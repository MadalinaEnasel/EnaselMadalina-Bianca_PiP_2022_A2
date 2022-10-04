# Find The greatest common divisor of multiple numbers read from the console.

def gcd(a, b):
    if (b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)
