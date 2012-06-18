#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def main():
    smallestNumber = 1
    
    for i in xrange(2, 20):
        smallestNumber = lcm(smallestNumber, i)

    print(smallestNumber)
    
def gcd(x, y):
    remainder = -1
    temp = 0

    if x < y:
        temp = y
        y = x
        x = temp
    
    while remainder != 0:
        remainder = x % y
        x = y
        y = remainder

    return x

def lcm(x, y):
    return (x * y) / gcd(x, y)
        
if __name__ == "__main__":
    main()
