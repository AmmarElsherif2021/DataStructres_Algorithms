# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 21:22:19 2023

@author: ammar
"""

class HashMap:
    def __init__(self):
        self._values=[None for item in range(256)]
        self._keys=[]
    def hashing(self,key):
        return hash(key) % len(self._keys)
    def __getitem__(self,key):
        if self._values[self.hashing(key)] is not None:
            return self._values[self.hashing(key)]
        else:
            return 'Not found'

    def __setitem__(self, key, value):
        # There must be a value
        if value is None:
            raise ValueError('None not permitted as a value')
        #There is value but never been inserted yet
        if self.hashing(key) not in self._keys:
            self._keys.append(self.hashing(key))
            self._values[self.hashing(key)]=value
        #inserted before but you wanna update it
        else:
            if self.hashing(key):
                self._values[self.hashing(key)] = value


