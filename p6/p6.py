#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math

def main():
    sumSquares = 0
    squareSum = 0
    numbers = range(1, 101)
    
    for i in numbers:
        sumSquares += i ** 2

    squareSum = sum(numbers) ** 2

    #    print(sum(numbers))
    print(squareSum)
    print(sumSquares)

    print(abs(squareSum - sumSquares))
    
        
if __name__ == "__main__":
    main()
