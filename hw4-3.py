'''
Luke R. Prescott
lprescott@albany.edu

This python program aims to solve question 2, part b on homework 4 in ICSI 401.

Output:
l_2(x) = 6.618210918382494x^2 + -1.1435233683025379x + 1.2355603697102275
S = 0.0014429128859326577
'''

#libraries used
import math
import numpy as np

def main():

    m = 10 #number of vals
    x_i = [4,4.2,4.5,4.7,5.1,5.5,5.9,6.3,6.8,7.1] #given xs
    y_i = [102.56,113.18,130.11,142.05,167.53,195.14,224.87,256.73,299.5,326.72] #given ys

    #initialize A, and b
    A = [[],[],[],[],[],[],[],[],[],[]]  
    b = [[],[],[],[],[],[],[],[],[],[]] 

    #add values to A and b
    for x in range(0, m):
        A[x].append(math.pow(x_i[x], 2))
        A[x].append(x_i[x])
        A[x].append(1)
        b[x].append(y_i[x])

    #A_np is the numpy array equivalent
    A_np = np.array(A, np.float64)

    #b_np is the numpy array equivalent
    b_np = np.array(b, np.float64)

    #Solve the system of normal equations
    x = np.linalg.lstsq(A_np, b_np, rcond=None)  

    #Print out the least square polynomial of degree 2
    print("l_2(x) = {}x^2 + {}x + {}".format(x[0][0][0], x[0][1][0], x[0][2][0]))

    #Store a, b, and c for error calculation
    a = x[0][0][0]
    b = x[0][1][0]
    c = x[0][2][0]

    #Calculate error
    error = 0
    for x in range (0, m):
        error += math.pow((y_i[x] - (a*math.pow(x_i[x], 2) + b*x_i[x] + c)), 2)

    #Print error
    print("S = {}".format(error))
          
if __name__ == "__main__":
    main()