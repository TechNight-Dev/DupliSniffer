#! /usr/bin/python

import os
import hashlib

class HashedFile():

    def __init__(self, path):
        if os.path.exists(path):
            self.path = path
        else:
            raise Error("File path does not exist")

        self.duplicate = False
        self.hash = self.calculate_hash()
        self.file_name = os.path.basename(self.path)

    def __eq__(self, other_hash):
        if isinstance(other_hash, HashedFile):
            return self.hash == other_hash.hash
        else:
            return False

    def calculate_hash(self, blocksize=65536):
        
        hasher = hashlib.md5()

        with open(self.path, 'rb') as a_file:
            buf = a_file.read(blocksize)
            
            while len(buf) > 0:
                hasher.update(buf)
                buf = a_file.read(blocksize)
        
        return hasher.hexdigest()

    def is_duplicate(self):
        self.duplicate = True

    def del_file():
        os.remove(self.path)

if __name__ == '__main__':
    a_file = HashedFile('/home/derpy/Coding/Python/Practice/os_walk.py')
    print(a_file.hash)
    second_file = HashedFile('/home/derpy/Coding/Python/Practice/os_walk.py')
    print(second_file.hash)
    if a_file == second_file:
        a_file.is_duplicate()
        second_file.is_duplicate()
        print("Duplicate")
    else:
        print('Not Duplicate')