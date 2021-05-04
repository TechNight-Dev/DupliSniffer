#! usr/bin/python


# https://www.geeksforgeeks.org/command-line-arguments-in-python/
# https://www.geeksforgeeks.org/command-line-interface-programming-python/
# https://realpython.com/command-line-interfaces-python-argparse/

import sys
import argparse
import os
from file_hash import HashedFile

def walk_path(dir_path: list) -> list:
    """ Take a path to a folder and then return a list of all files found in
        the folder. """

    # TODO: Would this work better with a generator?
    file_paths = []
    for root, subDirs, file_list in os.walk(dir_path):
        for filename in file_list:
            path = os.path.join(root, filename)
            file_paths.append(path)
    
    return file_paths

def find_dups(file_paths: list, hash_type: str = 'md5') -> dict:
    """ Create a dictionary from list of file paths with the file hash as key
        Value is a list of file paths with same hash"""

    hash_dict = {}
    for a_file in files:
        hashed_file = HashedFile(a_file, hash_type)
        if hashed_file.hash not in hash_dict:
            hash_dict[hashed_file.hash] = [hashed_file]
        else:
            hash_dict[hashed_file.hash].append(hashed_file)

    clean_dict = remove_nondups(hash_dict)
    
    return clean_dict

def remove_nondups(hash_dict: dict) -> dict:
    """ Removes any value in a dictionary that only contains one path """

    dups = {}
    for key, values in hash_dict.items():
        if len(values) > 1:
            dups[key] = values
            for value in values:
                value.is_duplicate()
    
    return dups

def create_log(content:dict, path:str = '.'):
    """ Create a text file containing list of hashes and duplicates """

    if not os.path.isdir(path):
        raise Error(f"{path} is not an existing directory")

    with open(os.path.join(path, "log.txt"), 'w') as log:
        log.write(content)

# Message displayed in the help menu
msg = "Used to find duplicate files by comparing hashes of files."
prog_name = "duplisniffer"

# Initialize the parser
parser = argparse.ArgumentParser(prog = prog_name,
                                 description = msg)

parser.add_argument('Path', metavar='path', type=str, nargs='+',
                    help="Path to directory to scan for duplicates")

# Add optional arguments below
parser.add_argument("-t", "--Type", help = "Choose the type of hash to use.")
parser.add_argument("-f", "--File", type = str, default = None,
                    help = "Returns hash of file")
parser.add_argument("-l", "--Log", type = str, default = None,
                    help = "Path to folder to store log file")

# Read the arguments provided
args = parser.parse_args()

if args.Type:
    files = walk_path(args.Path, args.Type)
else:
    files = walk_path(args.Path)

hash_dict = find_dups(files)
for key, values in hash_dict.items():
    print(key)
    for value in values:
        print("\t", value.path)


if args.Directories:
    print(f"Directories still being implemented.")

if args.File:
    print(f"File will be implemented")

if args.Log:
    print(f"Log feature will be implemented")