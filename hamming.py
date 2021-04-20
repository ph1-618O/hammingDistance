from PyDictionary import PyDictionary as wordDict
from english_words import english_words_set as words
import itertools
from itertools import permutations
import time
import random
import json
import pandas as pd

def getHamming():
    get_input = input('What two words would your like to get the Hamming Distance of?\n')
    str1 = get_input.split()[0]
    #assuming the input could be cat and bat, grabbing the first and last words
    str2 = get_input.split()[-1]
    confirm_words = input(f'Are your two words {str1} and {str2}? Y/N\n')
    if 'y' in confirm_words.lower():
        i = 0
        count = 0
        if len(str1) > len(str2):
            dif = len(str1) - len(str2)
            truncStr = str1[:-dif]
            while(i < len(truncStr)):
                if(truncStr[i] != str2[i]):
                    count += 1
                i += 1
            count += dif
            print(f'The hamming distance between {str1} and {str2} is {count}')
            return count
        elif len(str1) < len(str2):
            dif = len(str2) - len(str1)
            truncStr = str2[:-dif]
            while i < len(truncStr):
                if(truncStr[i] != str1[i]):
                    count += 1
                i += 1
            count += dif
            print(f'The hamming distance between {str1} and {str2} is {count}')
            return count
        else:
            while i < len(str1):
                if(str1[i] != str2[i]):
                    count += 1
                i += 1
            print(f'The hamming distance between {str1} and {str2} is {count}')
            return count
    else:
        print('Please try again.\n')
    
getHamming()   