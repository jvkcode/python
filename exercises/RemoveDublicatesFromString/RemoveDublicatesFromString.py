#!/usr/bin/env python
import sys

# O(n^2)
def RemoveDublicatesFromString(s):
    i, j = 0, 1
    found = 0
    while j != len(s):
        i = j-1
        found = 0
        while (i >= 0):
            if s[i] is s[j]:
                # remove duplicate
                s.pop(j)
                found = 1
                i = -1
            else:
                i -= 1
        if found is 0:
            j += 1

# O(n/2)    
def TwoPointerTechnique(s):
    n = len(s)-1
    i = 0
    while (i < n):
        if s[i] is s[n]:
            s.pop(n)
        i += 1
        n -= 1
        
def main():
    try:
        g = list(sys.argv[1])
    except IndexError:
        return
    if not g:
        return
    given = g
    print ("before %s" % given)
    RemoveDublicatesFromString(given)
    print ("(1) after %s" % given)
    
    given = g
    TwoPointerTechnique(given)
    print ("(2) after %s" % given)
        
if __name__ == '__main__': main()
    