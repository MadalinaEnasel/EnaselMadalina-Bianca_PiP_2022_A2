# Write a script that converts a string of characters written in UpperCamelCase into
# lowercase_with_underscores.

string=input("Your UpperCamelCase")
newString = string[0].lower()
j=1

for i in range(1,len(string)):
    if string[i].isupper():
        newString += '_' + string[i].lower()
    else:
        newString+=string[i]

print("My lowercase_with_underscores", newString)