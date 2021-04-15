'''Source: https://www.pythoncentral.io/finding-duplicate-files-with-python/'''
'''This is an example file of how to use the hashlib module to find duplicate
files. Essentially I am copying and commenting code that I found in the above
mentioned source.'''

import os
import sys
import hashlib #Allows us to find duplicate files even if name is different.

# This function calculates the MD5 hash of a given file.
# Receives path to file and returns HEX digest of file.
def hashfile(path, blocksize = 65536):
    """
    hashfile Generates an MD5 hash based on the provided file.

    Args:
        path (string): path to file to be hashed
        blocksize (int, optional): [description]. Defaults to 65536.

    Returns:
        string: MD5 hash of provided file
    """
    aFile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = aFile.read(blocksize)

    while len(buf) > 0:
        buf = aFile.read(blocksize)
    aFile.close()

    return hasher.hexdigest()

def findDup(parentFolder):
    """
    findDup Traverses a given folder to find duplicated files within and then
    stores them in a dictionary.

    Args:
        parentFolder (string): Path to folder user wants to scan for duplicates

    Returns:
        dict: Key is the MD5 hash, value is a list containing paths to the
        duplicate files.
    """
    dups = {}
    for root, subDirs, fileList in os.walk(parentFolder):
        print(f'Scanning {root}...')
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(root, filename)
            # Get the hash with 'hashfile' function
            fileHash = hashfile(path)
            if fileHash in dups:
                dups[fileHash].append(path)
            else:
                dups[fileHash] = [path]
    return dups

def joinDicts(dict1, dict2):
    """
    joinDicts Takes two dictionaries and combines them into one. Modifies a
    global dictionary

    Args:
        dict1 (dict): Global dictionary to modify
        dict2 (dict): Dictionary to compare against dict1 and see if there are
        duplicates or if new files need to be added.
    """
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key] # If file is duplicate append path to dict 1
        else:
            dict1[key] = dict2[key] # If file does not exist in dict1

def printResults(dict1):
    """
    printResults If there are duplicates in dict1, the path will be printed. If
    no duplicates are in dict1, we will be notified.

    Args:
        dict1 (dict): Key contains the MD5 hash of a file, the value is a list
        of paths to the file.
    """
    # If value of dict1 contains more than one string in list, store in results
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0: # Check to see if there are actually results
        print('Duplicates Found:')
        print('The following files are identical. The name may differ, but the \
            content is identical')
        print('___________________')
        for result in results:
            for subresult in result:
                print(f'\t{subresult}')
            print('___________________')
    else:
        print('No duplicate files found.')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        dups = {}
        folders = sys.argv[1:]
        for folder in folders:
            if os.path.exists(folder):
                joinDicts(dups, findDup(folder))
            else:
                print(f'{folder} is not a valid path. Verify')
                sys.exit()
        printResults(dups)
    else:
        print('Usage: python example.py <folder> or python example.py <folder1> <folder2> <folder3>')

# Doesn't check duplicates properly. Need to debug.git