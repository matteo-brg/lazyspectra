'''
 Desc  : Collection of utilities used in other codes 
'''

import os, errno
from operator import methodcaller
import numpy as np


class Config2Dict(object):
    '''
    This class is used to convert in dictionary a config file written in the form:
    
    field1 = value1
    field2 = value2

    '''
    def __init__(self, filename):
        if not os.path.exists(filename):
            raise IOError(errno.ENOENT, os.strerror(errno.ENOENT), filename)
            return
         
        self.__filename=filename
        self.__pars=dict()

        self.__open()
        
        return

    def get_parameters(self):
        return self.__pars

    def __open(self):
        with open(self.__filename) as f:
            # Read config file as a unique string
            text=f.read();
            
            # Remove all the comments and split the string in rows
            nocomments = [s.split('#')[0] for s in text.split('\n')]            
            
            # Find all the rows containing the character "=" 
            # and remove alle the whitespace
            matching = ["".join(s.split()) for s in nocomments if "=" in s]

            # Convert list in a map (list of list)
            entries=dict(list(map(methodcaller("split", "="), matching)))

            self.__pars.clear()

            # Check for float in the entries 
            self.__pars={d: float(entries[d]) if isfloat(entries[d]) else entries[d] for d in entries}

            # Check for list in the entries 
            self.__pars={d: self.__pars[d] if isfloat(self.__pars[d]) or not (',' in self.__pars[d])
                         else self.__pars[d].split(',') for d in self.__pars}

            # Check for float in the lists 
            self.__pars={d: self.__pars[d] if not isinstance(self.__pars[d], list)
                         else [float(l) if isfloat(l) else l for l in  self.__pars[d]]  for d in self.__pars}

            
        return
        

def fix_path(path):
    '''
    fix a str path
    '''
    if path[-1] != "/":
        path += "/"
    return path
    
    
'''
 Check if a string represents float value
''' 
def isfloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False    
    
def locate_word(array,word):
    '''
    given a numpy array of str, returns all the indexes of the entries which contain 'word' somewhere. Not very fast.
    
    e.g.: locate_word(["hi", "nice3", "is not nice", dude"], word='nice') = [1,2]
    '''
    i = 0
    temp = []
    for el in array:
        if el.find(word) != -1:
            temp.append(i)
        i+=1
    return np.array(temp)
    
def merge_dictionaries(dic1,dic2,keys=None):
    '''
    dic1 and dic2 are dictionaries of dictionary.
    If keys are None, keys are the common keys between dic1 and dic2.
    Else, keys are the key of dic1 which will be updated by dict2[key]. 
    '''
    dic3 = dic1.copy() #for safety
    if keys is None:
        keys = list(set(dic3).intersection(set(dic2)))
    for k in keys:
        dic3[k] = {**dic3[k] , **dic2[k]}
    return dic3
    
def log(message='',level=1):
    out = '|'+level*2*'-'
    if level==-1:
        out = '|'+20*'-'
    else:
        out +=' '+ message
    if level == 0:
        out = message
    print(out)
    return


def findOccurrences(s, ch):
    '''
    Find all the occurences of a character (ch) in a string (s)
    '''
    return [i for i, letter in enumerate(s) if letter == ch]
