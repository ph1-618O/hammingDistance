from PyDictionary import PyDictionary as wordDict
from english_words import english_words_set as words
import itertools
from itertools import permutations
import time
import random
import json
import pandas as pd

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res

wordsList =[]
with open('wordsAlpha.txt', 'r') as wordsFile:
    for word in wordsFile:
        wordsList.append(word.rstrip())

# Trying to move away from globals into being more comfortable with dictionaries
def make_dict(letter):
    alphaDict = {}
    wordsList =[]
    with open('wordsAlpha.txt', 'r') as wordsFile:
        for word in wordsFile:
            wordsList.append(word.rstrip())
    holder = []
    for i in wordsList:
        if i.startswith(letter):
            holder.append(i)
            alphaDict[letter] = holder
    return alphaDict

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_dlist = []
for i in alpha:
    alpha_dlist.append(make_dict(i))

alpha_dict = alpha_dlist[0]
for i in range(len(alpha_dlist)):
    if i < len(alpha_dlist)-1:
        alpha_dict = Merge(alpha_dict, alpha_dlist[i+1]) 

alpha_df = pd.DataFrame.from_dict(alpha_dict, orient='index').T


# Davids code
def assess_NA(data):
    null_sum=data.isnull().sum()
    total = null_sum.sort_values(ascending=False)
    percent = ( ((null_sum / len(data.index))*100).round(2) ).sort_values(ascending=False)
    df_NA = pd.concat([total, percent], axis=1, keys=['Number of NA', 'Percent NA'])
    df_NA = df_NA[ (df_NA.T != 0).any() ]
    
    return df_NA


# How many Nans are there to check to see if code worked
sums = 0
total_na = alpha_df.isnull().sum()
for i in total_na:
    sums += i
if (len(alpha_df)*26)-len(wordsList) == sums:
    print('The dataframe and wordsList entries are the same, there are just added NaNs')