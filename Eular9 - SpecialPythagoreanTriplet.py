#Eular 9: Special Pythagorean Triplet

def pythagorean(n):
    for i in range(1,n):
        for j in range(i,n):
            k = j+1
            while k*k < j*j + i*i:
                k = k+1
            if k*k == j*j + i*i and k+j+i == n:
                print(i*j*k, end=' ')
                return
