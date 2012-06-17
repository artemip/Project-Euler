#Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    largestPalindrome = -1
    for i in xrange(100, 999):
        for j in xrange(100, 999):
            possiblePalindrome = i * j
            if isPalindrome(possiblePalindrome) and possiblePalindrome > largestPalindrome:
                largestPalindrome = possiblePalindrome
                
    print largestPalindrome

def isPalindrome(n):
    nString = str(n)
    i = 0
    j = len(nString) - 1

    while i < j:
        if nString[i] != nString[j]:
            return False
        i += 1
        j -= 1

    return True

if __name__ == "__main__":
    main()
