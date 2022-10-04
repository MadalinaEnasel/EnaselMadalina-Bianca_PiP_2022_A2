# Write a script that calculates how many vowels are in a string.

string = input ("Give me a phrase")
no=0

def isVowel(x):
    if (x == 'a' or x == 'e' or
            x == 'i' or x == 'o' or x == 'u'):
        return True
    else:
        return False

for i in string.lower():
    if isVowel(i):
        no+=1
print(no)
num_vowels=0
for i in string:
    if i in "aeiouAEIOU":
        num_vowels += 1