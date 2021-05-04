#! /usr/bin/python

# https://www.programcreek.com/python/example/102910/hashlib.algorithms_guaranteed

import os
import hashlib

# TODO: Eventually add changing the type of hash used.
# Need to figure out what hashes are available
# Most likely use a dictionary to store types and the functions used.
# {'md5': hashlib.md5(), }

class HashedFile():

    def __init__(self, path, hash_type=None):
        self.path = path
        if not os.path.exists(self.path):
            raise Exception("File path does not exist")

        if hash_type == None:
            self.hash_type = 'md5'
        else:
            self.hash_type = hash_type.lower()
            
        if self.hash_type not in hashlib.algorithms_guaranteed:
            raise Exception(f"Algorithm '{hash_type}' is not supported")
        
        self.duplicate = False
        self.hash = self.calculate_hash()
        self.file_name = os.path.basename(self.path)


    def __eq__(self, other_hash):
        if isinstance(other_hash, HashedFile):
            return self.hash == other_hash.hash
        else:
            return False

    def calculate_hash(self, blocksize=65536):
        
        hasher = getattr(hashlib, self.hash_type)()

        with open(self.path, 'rb') as a_file:
            buf = a_file.read(blocksize)
            
            while len(buf) > 0:
                hasher.update(buf)
                buf = a_file.read(blocksize)
        
        return hasher.hexdigest()

    def is_duplicate(self):
        self.duplicate = True

    def del_file(self):
        os.remove(self.path)

    def get_file_type(self):
        pass

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