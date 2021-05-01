#! usr/bin/python


# https://www.geeksforgeeks.org/command-line-arguments-in-python/
# https://www.geeksforgeeks.org/command-line-interface-programming-python/
# https://realpython.com/command-line-interfaces-python-argparse/

import sys
import argparse
from file_hash import HashedFile

def 

# Message displayed in the help menu
msg = "Used to find duplicate files by comparing MD5 hashes of files."
prog_name = "duplisniffer"

# Initialize the parser
parser = argparse.ArgumentParser(prog = prog_name,
                                 description = msg)

parser.add_argument('Path', metavar='path', type=str,
                    help="Path to directory to scan for duplicates")

# Add optional arguments below
parser.add_argument("-t", "--Type", help = "Choose the type of hash to use.")
parser.add_argument("-d", "--Directories", type = str, default = None,
                    help = "Path to folder(s) to scan for duplicates")
parser.add_argument("-f", "--File", type = str, default = None,
                    help = "Returns hash of file")
parser.add_argument("-l", "--Log", type = str, default = None,
                    help = "Path to log file.")

# Read the arguments provided
args = parser.parse_args()

if args.Path:


if args.Type:
    print(f"This is a work in progress. Eventually {args.Type} will be added")

if args.Directories:
    print(f"Directories still being implemented.")

if args.File:
    print(f"File will be implemented")

if args.Log:
    print(f"Log feature will be implemented")