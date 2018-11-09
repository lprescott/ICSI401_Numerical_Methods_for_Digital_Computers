import math
import numpy as np
import sys

# Luke R. Prescott
# 11/08/2018
# Newton's Method for solving a System of Equations
# This program uses Gaussian Elimination to solve the given non-linear system of equations using Newton's method.
def main():

    #Redirect stdout to a document
    sys.stdout = open('solvedSystem.doc', 'w')

    #Given functions:
    #f(x,y) = x^2+xy^3=9  \
    #g(x,y) = 3x^2-y^3=4  / p(x,y)

    #Manually calculated jacobian matrix:
    #| 2x+y^3 3xy^2     |
    #| 6xy    3x^2-3y^2 |

    #Other given info:
    initialGuess = [2.98, 0.15]
    x_k = initialGuess[0]
    y_k = initialGuess[1]

    error = float(10) * math.pow(10, -12)

    #Default the values of x for the next iteration.
    x_k1 = 0
    y_k1=0

    #Print the title bar
    print('| {:>5} | {:>22} | {:>22} | {:>22} | {:>22} | {:>22} |\n'.format("k", "x_k", "y_k", "x_k+1", "y_k+1", "x_k+1 - x_k"))

    #Set difference, to use as a flag, as a arbitrarily high number
    difference = 100

    #For the given number of iterations
    for count in range(0, 4):
        
        #For every iteration except the first
        if(count!=0):

            #A is the matrix A, the jacobian of the given system
            A = jacobian(x_k, y_k)
            #A_np is the numpy array equivalent
            A_np = np.array(A)

            #b is the matrix b, the negated given system
            b = givenSystem(x_k, y_k)
            #b_np is the numpy array equivalent
            b_np = np.array(b)

            #Call numpy's (np) method linalg to solve a linear matrix equation pass A and B
            x = np.linalg.solve(A_np, b_np)

            #set deltaX and deltaY to position x_11 and x_21 in the returned 1x2 matrix
            deltaX = x[0][0]
            deltaY = x[1][0]

            #Increment x_k and y_k by their changed values
            x_k += deltaX
            y_k += deltaY

        #On all iterations
        #Find the next values for x and y for printing of table
        x_k1 = x_k + np.linalg.solve(np.array(jacobian(x_k, y_k)), np.array(givenSystem(x_k, y_k)))[0][0]
        y_k1 = y_k + np.linalg.solve(np.array(jacobian(x_k, y_k)), np.array(givenSystem(x_k, y_k)))[1][0]

        #Calculate the difference between x_k and x_k+1
        difference = math.fabs(x_k1 - x_k)

        #print table row
        print('| {:>5} | {:>22} | {:>22} | {:>22} | {:>22} | {:>22} |'.format(count, x_k, y_k, x_k1, y_k1, difference))

        #increment count
        count += 1

    #This checks if the found Ax=b matrix equation checks.
    if(np.allclose(np.dot(A_np, x), b_np)):
        print("Ax=b checks!")
    else:
        print("Ax=b fails!")
    
    #This checks if the error tolerance checks
    if(difference < error): 
        print("|x_1 - x_k| < 10e-10 checks!")
    else:
        print("|x_1 - x_k| < 10e-10 fails!")
    

#This functions finds the jacobian of the given system as a matrix
def jacobian(x_k, y_k):
    #j_row,column
    j_11 = 2 * x_k + math.pow(y_k, 3)
    j_12 = 3 * x_k * math.pow(y_k, 2)
    j_21 = 6 * x_k * y_k
    j_22 = 3 * math.pow(x_k, 2) - 3 * math.pow(y_k, 2)
    return [[j_11, j_12],[j_21, j_22]]

#This function finds the negated system as a matrix
def givenSystem(x_k, y_k):
    #p_row,column
    p_11 = -1 * ( math.pow(x_k,2) + x_k * math.pow(y_k, 3) - 9 )
    p_21 = -1 * ( 3 * math.pow(x_k, 2) * y_k - math.pow(y_k, 3) - 4 )
    return [[p_11], [p_21]]

#For Tests
#This prints a two dimensional array
def printMatrix(matrix):
    for row in matrix:
        for val in row:
            print('{:<20}'.format(val), end=' ')
        print()
    print()
            
if __name__ == "__main__":
    main() 