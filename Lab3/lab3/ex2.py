#       2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def isPrime(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False


def primeArray(array):
    p_array = []
    for i in array:
        if isPrime(i):
            p_array.append(i)

    return p_array


a = primeArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 23, 34, 45, 56, 6778, 89])

print(a)
