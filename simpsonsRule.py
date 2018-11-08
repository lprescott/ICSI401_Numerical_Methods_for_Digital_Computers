import math
import sys


def main():

    sys.stdout = open('simpsonsRuleOutput.doc', 'w')

    #Given values:
    a = float(0)
    b = float(1)
    subdivisions = [2, 4, 8, 16, 32, 64, 128, 256]

    correctAnswer = 2 / 7
    print() #newline

    count = 0

    absRatio = 0
    relRatio = 0

    absErrors = []
    relErrors = []

    print('| {:>5} | {:>25} | {:>25} | {:>25} | {:>25} |\n'.format("n", "estimation", "absolute error", "relative error", "ratio of error"))
    for n in subdivisions:

        estimation = simpsonsRule(n, a, b)
        absoluteError = correctAnswer - estimation
        relativeError = (correctAnswer - estimation) / correctAnswer

        absErrors.append(absoluteError)
        relErrors.append(relativeError)
    
        if(count!=0):
            absRatio = absErrors[count] / absErrors[count-1]
            relRatio = relErrors[count] / relErrors[count-1]

            print('| {:>5} | {:>25} | {:>25} | {:>25} | {:>25} |'.format(n, estimation, absoluteError, relativeError, relRatio))
        else:
            print('| {:>5} | {:>25} | {:>25} | {:>25} | {:>25} |'.format(n, estimation, absoluteError, relativeError, "N/A"))
        count += 1
    print() #newline

def changeInX(n, a, b):
    return (b-a) / n

def simpsonsCoefficient(n, a, b):
    return changeInX(n, a ,b) / 3

def givenFunction(x):
    return math.pow(x, (5/2))

def simpsonsRule(n, a, b):
    deltaX = changeInX(n, a ,b)
    coefficient = simpsonsCoefficient(n, a, b)
    
    sum = 0
    x_a = 0
    for x in range(0, n+1):

        if(x==0):
            sum+=givenFunction(x_a)
        elif(((x%2)==1) and (x != n)): #odd
            sum+=givenFunction(x_a) * 4
        elif(((x%2)==0) and (x != n)): #even
            sum+=givenFunction(x_a) * 2
        else:
            sum+=givenFunction(x_a)
        x_a += deltaX
    return(sum * coefficient)

if __name__ == "__main__":
    main()