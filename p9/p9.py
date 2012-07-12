# There exists exactly one Pythagorean triplet (a^2 + b^2 == c^2) for which a + b + c = 1000.
# Find the product abc.
import math

def main():
        largest = 1000
        for a in xrange(1, largest):
                for b in xrange(a, largest):
                        if ( 1000 * ( a + b ) - ( a * b ) ) == 500000: #Post-simplification
                                c = math.sqrt(a**2 + b**2)
                                print(a * b * c)
     
if __name__ == "__main__":
    main()
