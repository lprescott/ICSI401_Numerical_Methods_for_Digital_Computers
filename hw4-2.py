'''
Luke R. Prescott
lprescott@albany.edu

This python program aims to solve question 2, part a on homework 4 in ICSI 401.

Output:
l_1(x) = -194.13824073209292 + 72.08451769539633x
S = 329.01319303389823
'''

#libraries used
import math

def main():

    m = 10 #number of vals
    x_i = [4,4.2,4.5,4.7,5.1,5.5,5.9,6.3,6.8,7.1] #given xs
    y_i = [102.56,113.18,130.11,142.05,167.53,195.14,224.87,256.73,299.5,326.72] #given ys

    #These for-loops calculate the summations used in the derived expression for a 
    #   degree 1 approximation
    sumOfYs = 0
    for x in range(0, m):
        sumOfYs += y_i[x]

    sumOfXsSquared = 0
    for x in range(0, m):
        sumOfXsSquared += math.pow(x_i[x], 2)

    sumOfXs = 0
    for x in range (0, m):
        sumOfXs += x_i[x]

    sumOfXbyY = 0
    for x in range(0, m):
        sumOfXbyY += (x_i[x] * y_i[x])

    #Calculate coefficient a and b, using the derived expressions for a degree 1 approximation
    a = (sumOfYs * sumOfXsSquared - sumOfXs * sumOfXbyY) / (m * sumOfXsSquared - math.pow(sumOfXs, 2))
    b = (m * sumOfXbyY - sumOfXs * sumOfYs)/(m * sumOfXsSquared - math.pow(sumOfXs, 2))

    #Print out the least square polynomial of degree 1
    print("l_1(x) = {} + {}x".format(a, b))

    #Calculate error
    error = 0
    for x in range (0, m):
        error += math.pow((y_i[x] - (a + b*x_i[x])), 2)

    #Print error
    print("S = {}".format(error))

if __name__ == "__main__":
    main()