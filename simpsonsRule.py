import openpyxl
import math

def main():

    #Given:
    a = 0
    b = 5
    subdivisions = [2, 4, 8, 16, 32, 64, 128, 256]

    for n in subdivisions:
        print(n)
        simpsonsRule(n, a, b)

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
        elif(((x%2)==1) and (x != n)):
            sum+=givenFunction(x_a) * 4
        elif(((x%2)==0) and (x != n)):
            sum+=givenFunction(x_a) * 2
        else:
            sum+=givenFunction(x_a)

        x_a += deltaX

    print(sum * coefficient)

if __name__ == "__main__":
    # execute only if run as a script
    main()