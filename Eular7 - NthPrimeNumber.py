#Eular 7: Find nth Prime number


# Function to test if number is Prime
def prime(n):
    j = 2
    while j*j <= n:
        if n%j == 0:
            return False
        j += 1
    return True

# Finding nth Prime Number
def nthPrime(n):
    i = 2
    ncnt = 0
    while(1):
        if prime(i):
            ncnt += 1
        if ncnt == n:
            print(i)
            break
        i += 1
