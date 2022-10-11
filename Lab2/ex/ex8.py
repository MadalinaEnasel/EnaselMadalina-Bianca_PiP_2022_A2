#Write a function that counts how many bits with value 1 a number has. For example for number 24,
# the binary format is 00011000, meaning 2 bits with value "1"

def suma_bin(num):
    suma = 0
    while num > 1:
        suma += num % 2
        num = int(num/2)
    return suma+1

print (suma_bin(35456))