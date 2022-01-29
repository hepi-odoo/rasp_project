import sys

def fibo(n):
    i = 0
    current = 0
    previous = 1
    for i in range(1, n):
        temp = current
        current += previous
        previous = temp
        # print(current)
    print(current)

if __name__=="__main__":
    n = int(sys.argv[1])
    # print(arg)
    fibo(n)

