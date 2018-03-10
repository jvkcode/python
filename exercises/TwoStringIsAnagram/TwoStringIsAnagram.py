#!/usr/bin/env python

# check if two given string is anagram:
# 1 - the same number of characters in both strings;
# 2 - the same set of charactes in both strings;

# anagram example:
# Damon Albarn
# Dan Abnormal

from __future__ import print_function
import sys

def InitDictionary(count):
    for c in "abcdefghijklmnopqrstuvwxyz":
        count[c] = 0

def SetDictionaryValue(c, count):
    count[c] += 1

def CheckString(l, count):
    for c in l:
        if c == ' ' or c == '\n':
            continue
        SetDictionaryValue(c.lower(), count)
       
def IsAnagram(count):
    for c in "abcdefghijklmnopqrstuvwxyz":
        if count[c]%2 == 0:
            continue
        print("Not anagram: Character '{}' occur {} times".format(c, count[c]))
        return 1
    print("\nis anagram")
    return 0
    
def main():
    try:
        f = sys.argv[1]
    except IndexError:
        print("Missing command line argument - file name")
        return
    count = {}
    InitDictionary(count)
    try:
        with open(f,"r") as outfile:
            for line in outfile:
                print(line, end='')
                l = list(line)
                CheckString(l,count)
            IsAnagram(count)
                 
    except IOError, err:
        print (err)
        return
    
if __name__ == '__main__': main()