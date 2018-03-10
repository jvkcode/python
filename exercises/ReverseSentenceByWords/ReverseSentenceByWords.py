#!/usr/bin/env python

# revert string by words
# INPUT:
# "---------- Ice and Fire ------------",
# "                                    ",
# "fire, in end will world the say Some",
# "ice. in say Some                    ",
# "desire of tasted I've what From     ",
# "fire. favor who those with hold I   ",
# "                                    ",
# "... elided paragraph last ...       ",
# "                                    ",
# "Frost Robert -----------------------",
#
# OUTPUT:
# ------------ Fire and Ice ----------
#
# Some say the world will end in fire,
# Some say in ice.
# From what I've tasted of desire
# I hold with those who favor fire.
#
# ... last paragraph elided ...
# 
# ----------------------- Robert Frost

# 1: INPUT: Ice and Fire
# 2: Reverse all string: eriF dna ecI
# 3: Reverse each word in string: Fire and Ice
# 4: OUTPUT: Fire and Ice

from __future__ import print_function
import sys


def ReverseString(s,l,r):
    if s[r] == '\n':
        r -= 1
    while( l < r):
        # do not revert if the same
        if s[l] == s[r]:
            l += 1
            r -= 1
            continue
        temp = s[l]
        s[l] = s[r]
        s[r] = temp
        l += 1
        r -=1
 
def ReverseWords(s,l):
    left, i = 0, 0
    while (i < l):
        if s[i] == ' ' or s[i] == '\n':
            # do not revert if length one char
            if left == i-1:
                left = i+1
                i += 2
            else:
                # reverse word
                ReverseString(s, left, i-1)
                i += 1
                left = i
        else:
            i += 1
    
    
def main():
    try:
        f = sys.argv[1]
    except IndexError:
        print ("Misssing command line argument\n")
        return
    try: 
        with open(f, 'r') as infile:
            for line in infile:
                # convert string to list
                l = list(line)
                z = len(l)
                #print("before: %s" % "".join(l))
                ReverseString(l, 0, z-1)
                #print("ReverseString: %s" % "".join(l), end='')
                ReverseWords(l, z)
                #print("ReverseWords: %s" % "".join(l))
                print("".join(l), end='')

    except IOError, err:
        print (err)
      
if __name__ == '__main__': main()    
    