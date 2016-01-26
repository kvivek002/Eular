#Eular 4: Largest palindrome product

def palindromeNumber():
    palindrome = []
    for i in range(100,999):
        for j in range(100,999):
            pal = i*j
            if str(pal) == str(pal)[::-1]:    # String reversal in Python
                palindrome.append(pal)
    print(max(palindrome))