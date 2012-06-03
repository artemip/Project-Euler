def main():
    print Sum(3) + Sum(5) - Sum(15)

def Sum(n):
    i = n
    result = 0
    
    while i < 1000:
        result += i
        i += n
    
    return result

if __name__ == '__main__':
    main()
