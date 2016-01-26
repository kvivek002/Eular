# Eular 1: Multiple of 3 and 5


def m35(n):
    sum = 0
    for i in range(1,n):
        if i%3 == 0:
            sum = sum + i
            print(i, end=' ')
        elif i%5 == 0:
            sum = sum + i
            print(i, end=' ')
    print("\nSum of multiples of 3 or 5 below ",n," is ",sum)

