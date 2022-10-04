# Find The greatest common divisor of multiple numbers read from the console.

def gcd(a, b):
    if (b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)

no_numbers= int(input("How many numbers are you planning on giving?"))
numbers = [None]*no_numbers

for i in range(no_numbers):
    numbers[i] = int(input("What number would you like to give?"))

finalGcd = gcd(numbers[0],numbers[1])
for i in range(2,len(numbers)):
    finalGcd= gcd(finalGcd,numbers[i])

print(finalGcd)