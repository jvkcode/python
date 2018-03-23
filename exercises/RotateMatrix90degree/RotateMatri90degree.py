#!/usr/bin/env python
# rotate anti-clockwise given matrix 90%
#Input
# 1  2  3
# 4  5  6
# 7  8  9
#
#Output:
# 3  6  9 
# 2  5  8 
# 1  4  7 
#
#Input:
# 1  2  3  4 
# 5  6  7  8 
# 9 10 11 12 
#13 14 15 16 
#
#Output:
# 4  8 12 16 
# 3  7 11 15 
# 2  6 10 14 
# 1  5  9 13
#
# First row of source -> First column of destination, elements filled in opposite order
# Second row of source ->Second column of destination, elements filled in opposite order
# so on
# Last row of source -> Last column of destination, elements filled in opposite order.
#
# An N x N matrix will have floor(N/2) square cycles. 


from __future__ import print_function

def InitMatx(m,n):
    i = 1
    for x in range(0,n):
        for y in range(0,n):
            m[x][y] = i
            i += 1
        

def PrintMatx(m,n):
    for x in range(0,n):
        for y in range(0,n):
            print("{0:2d}".format(m[x][y]), end=' ')
        print("")
    print("")

def RotateAntiClockwise90egree(m, n):
    t = 0
    print("Anticlockwise 90%: coordinates(vetical,horisontal)")
    for a in range(0,int(n/2)):
        for y in range(a, n-1-a):
            #save top cell from left
            t = m[a][y]
            print("saved anticlockwise: t={} a({}) y({})".format(t,a,y))
            PrintMatx(m,n)
            
            # move right -> top
            m[a][y] = m[y][n-1-a]
            print("(1) anticlockwise: (a{},y{}) = (y{}),n-1-a({}) ".format(a,y,y,n-1-a))
            PrintMatx(m,n)
            
            # move bottom -> right
            m[y][n-1-a] = m[n-1-a][n-1-y]
            print("(2) anticlockwise: y({}),n-1-a({}) = n-1-a({}),n-1-y({})".format(y,n-1-a,n-1-a,n-1-y))
            PrintMatx(m,n)
            
            # move left -> bottom
            m[n-1-a][n-1-y] = m[n-1-y][a]
            print("(3) anticlockwise: n-1-x({}),n-1-y({})  = n-1-y({}),x({})".format(n-1-a,n-1-y,n-1-y,a))
            PrintMatx(m,n)
            
            # assing top right -> bottom right
            m[n-1-y][a] = t
            print("(4) anticlockwise: n-1-y({}),a({}) = (a{},y{})".format(n-1-y,a,a,y))
            PrintMatx(m,n)
    
def RotateClockwise90egree(m, n):
    t = 0
    print("Clockwise 90%: coordinates(vetical,horisontal)")
    r=1
    for a in range(0,int(n/2)):
        for h in range(a, n-1-a):
            # save top-left
            t = m[a][h]
            print("save clockwise t={} a{} h{}".format(t,a,h))
            PrintMatx(m,n)
            
            # save bottom-left to the top
            m[a][h] = m[n-1-a][a]
            print("(1-{}) clockwise: (a{},h{} = n-1-a{},h{})".format(r,a,h,n-1-a,h))
            PrintMatx(m,n)
            
            # save bottom-left to bottom-right
            m[n-1-a][h] = m[n-1-a][n-1-h]
            print("(2-{}) clockwise: (n-1-v{},h{} = n-1-v{},n-1-h{})".format(r,n-1-v,h,n-1-v,n-1-h))
            PrintMatx(m,n)
            
            # save top-right to bottom-right
            m[n-1-v][n-1-h] = m[v][n-1-h] 
            print("(3-{}) clockwise (n-1-v{},n-1-h{} = v{},n-1-h{})".format(r,n-1-v,n-1-h,v,n-1-h))
            PrintMatx(m,n)
            
            # save saved top-left to top-right
            m[v][n-1-h] = t
            print("(4-{}) clockwise (v{},n-1-h{} = v{},h{})".format(r,v,n-1-h,v,h))
            PrintMatx(m,n) 
            
            r += 1
          
def main():
    N = 4
    # declare matrix based on N each element is 0
    matx = [ [ 0 for x in range(N) ] for y in range(N)]
    
    InitMatx(matx,N)
    print("Given: matrix {}x{}".format(N,N))
    PrintMatx(matx,N)
    given = matx
    RotateAntiClockwise90egree(given, N)
    given = matx
    RotateClockwise90egree(given, N)
    
    
if __name__ == '__main__': main()