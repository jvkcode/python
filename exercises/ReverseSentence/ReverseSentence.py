#!/usr/bin/env python

import sys

def ReverseSentence(s):
    left = 0
    right = len(s)-1
    
    while left < right:
        c = s[left]
        s[left] = s[right]
        s[right] = c
        right -= 1
        left += 1
    
def main():
    given = list(sys.argv[1])
    if not given:
        return
    print("before %s" % given)
    ReverseSentence(given)
    print("after %s" % given)
    
if __name__ == '__main__': main()