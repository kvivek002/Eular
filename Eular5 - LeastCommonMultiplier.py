#Eular 5: Least Common Multiplier

'''Formulae
   lcm(a,b) = (a*b) / gcd(a,b)
   gcd is calculated by Euclid’s algorithm.'''



def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b        # Euclid’s Algorithm
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)        # Calculating lcm

def lcmm(*args):
    """Return lcm of args."""
    import functools
    return functools.reduce(lcm, args)        # Python Recursion

'''
Function call:
lcmm([1,2,3,4,5]) 
'''
