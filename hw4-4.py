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
    x = [[0],[0],[0],[0],[0]]

    #Matrix b (Given)
    b = [[6],[6],[-6],[6],[6]]

    #Errror Tolerance TOL (Given)
    TOL = math.pow(10, -3)

    #Maximum number of iterations (Given)
    N = 25

    #A_np is the numpy array equivalent
    A_np = np.array(A, np.float64)

    #b_np is the numpy array equivalent
    b_np = np.array(b, np.float64)

    #x_np is the numpy array equivalent
    x_np = np.array(x, np.float64)

    #print title bar
    print('| {:>5} | {:>10} | {:>10} | {:>10} | {:>10} | {:>10} | {:>10} | {:>10} | {:>10} | {:>10} | {:>10} |\n'.format("k", "x_1", "x_2", "x_3", "x_4", "x_5", "x_1 error", "x_2 error", "x_3 error", "x_4 error", "x_5 error"))


    for k in range(0, N):
        #x_1
        x[0][0] = (1/A[0][0]) * (b[0][0] - A[0][1] * x[1][0] - A[0][2] * x[2][0] - A[0][3] * x[3][0] - A[0][4] * x[4][0])
        #x_2
        x[1][0] = (1/A[1][1]) * (b[1][0] - A[1][0] * x[0][0] - A[1][2] * x[2][0] - A[1][3] * x[3][0] - A[1][4] * x[4][0])
        #x_3 
        x[2][0] = (1/A[2][2]) * (b[2][0] - A[2][0] * x[0][0] - A[2][1] * x[1][0] - A[2][3] * x[3][0] - A[2][4] * x[4][0])
        #x_4
        x[3][0] = (1/A[3][3]) * (b[3][0] - A[3][0] * x[0][0] - A[3][1] * x[1][0] - A[3][2] * x[2][0] - A[3][4] * x[4][0])
        #x_5 
        x[4][0] = (1/A[4][4]) * (b[4][0] - A[4][0] * x[0][0] - A[4][1] * x[1][0] - A[4][2] * x[2][0] - A[4][3] * x[3][0])

        #x_np is the numpy array equivalent
        x_np = np.array(x, np.float64)

        #error is the distance the current solution is from zero
        error = np.dot(A_np, x_np) - b_np


        #print iteration
        print('| {:>5} | {:>10} | {:>10} | {:>10} | {:>10} | {:>10} | {:>10} | {:>10} | {:>10} | {:>10} | {:>10} |\n'.format(k, round(x[0][0], 10), round(x[1][0], 10), round(x[2][0], 10), round(x[3][0], 10), round(x[4][0], 10), round(error[0][0], 10), round(error[1][0], 10), round(error[2][0], 10), round(error[3][0], 10), round(error[4][0], 10)))

        #break out of loop if needed
        
        if((abs(error[0][0]) < TOL) and (abs(error[1][0]) < TOL) and (abs(error[2][0]) < TOL) and (abs(error[3][0]) < TOL) and (abs(error[4][0]) < TOL)):
            break

 

if __name__ == "__main__":
    main()