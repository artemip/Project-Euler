def main():
    print(fib(4000000))

def fib(n):
    i = 1
    j = 2
    tmp = i
    result = 0
    
    while j < n:
        if (j % 2 == 0): result += j
        
        tmp = j
        j = i + j
        i = tmp

    return result

if __name__ == '__main__':
    main()
