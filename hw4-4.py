'''
Luke R. Prescott
lprescott@albany.edu

This python program aims to solve question 3 on homework 4 in ICSI 401.

Output:


'''

#libraries used
import math
import numpy as np

def main():
    #Matrix A (Given)
    A = [[4,1,1,0,0],[-1,-3,1,1,0],[2,1,5,-1,-1],[-1,-1,-1,4,0],[0,2,-1,1,4]]

    #Initial guess of all zeros
    x = [0,0,0,0,0]

    #Matrix b (Given)
    b = [6,6,-6,6,6]

    #Errror Tolerance TOL (Given)
    TOL = math.pow(10, -3)

    #Maximum number of iterations (Given)
    N = 25

    for k in range(0, N):
        #x_1
        x[0] = (1/A[0][0]) * (b[0] - A[0][1] * x[1] - A[0][2] * x[2] - A[0][3] * x[3] - A[0][4] * x[4])
        #x_2
        x[1] = (1/A[1][1]) * (b[1] - A[1][0] * x[0] - A[1][2] * x[2] - A[1][3] * x[3] - A[1][4] * x[4])
        #x_3 
        x[2] = (1/A[2][2]) * (b[2] - A[2][0] * x[0] - A[2][1] * x[1] - A[2][3] * x[3] - A[2][4] * x[4])
        #x_4
        x[3] = (1/A[3][3]) * (b[3] - A[3][0] * x[0] - A[3][1] * x[1] - A[3][2] * x[2] - A[3][4] * x[4])
        #x_5 
        x[4] = (1/A[4][4]) * (b[4] - A[4][0] * x[0] - A[4][1] * x[1] - A[4][2] * x[2] - A[4][3] * x[3])
 
    print(x)

if __name__ == "__main__":
    main()