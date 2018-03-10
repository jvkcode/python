#!/usr/bin/python

# check if two scrings is anangram
# check how many changes were done for the second string

# anagram example:
# Damon Albarn
# Dan Abnormal

from __future__ import print_function
import sys

class Anagram:
    def __init__(self, v1, v2):
        self.a1 = v1
        self.a2 = v2
        
    def diff_index(self):
        i = 0
        count = 0
        l = len(self.a1)-1
        while i < l:
            if self.a1[i] != self.a2[i]:
                count += 1
            i += 1
        return count

def ReadFromFile(f):
    try:
        with open(f, 'r') as outfile:
            i = 0
            for line in outfile:
                if i == 0:
                    v1 = line
                    i += 1
                elif i == 1:
                    v2 = line
                    i += 1
                else:
                    print ("Invalid file format - file has extra lines while it should be two lines")
                    return (0, 0)
    except IOError, err:
        print(err)
        return (0, 0)                

    return (v1, v2)

def main():
    try:
        f = sys.argv[1]
    except IndexError:
        print("Missing command line argument - file name")
        return
    
    (a1, a2) = ReadFromFile(f)
    if a1 == 0:
        return
    l = len(a1)-1
    if l!= len(a2):
        print("{}{}\nis not anagram".format(a1, a2))
        return
    
    anagram = Anagram(a1,a2)
    
    # check how many changes have been done
    changed=anagram.diff_index()
    print("{}{}\nTotal changes: {}".format(a1,a2,changed))
   
    
    
if __name__ == '__main__': main()
  