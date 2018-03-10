#!/usr/bin/env python

# Replace ' ' in given string with '%20'

def main():
    g = "Missing command line argument: any string"
    print(g)
    l = list(g)
    i=0
    v = """%20"""
    for c in l:
        if c == ' ':
            l[i] = v[0]
            l.insert(i+1,v[1:])
            i += 1
        else:
            i+= 1
    print("".join(l))
    
if __name__ == '__main__': main()