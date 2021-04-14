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