#Euler 10: Summation of Primes

#Function to test if number is Prime    #Sieve?
def prime(n):
    j = 2
    while j*j <= n:
        if n%j == 0:
            return False
        j += 1
    return True
            

def sumPrime(n):
    psum = 2
    for i in range(3,n,2):
        if prime(i):
            psum = psum + i
    print(psum)
