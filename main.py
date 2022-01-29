
import sys
import threading


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
    # fibo(n)
    th = []
    for i in range(4):
        th.append(threading.Thread(target=fibo, args=(n,)))
    for i in range(4):
        th[i].start()

    for i in range(4):
        th[i].join()

