#Eular 6: Sum square difference

def sumSquareDif(n):
    return int(( ((n * (n+1)) / 2) ** 2 ) - ( (n * (n+1) * (2*n+1)) / 6 ))

#Formula used for sum of first n numbers and sum of square of first n numbers