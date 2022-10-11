# Write a function that validates if a number is a palindrome.

number = int(input("Ok, what number do you want to check?"))


def isPalindrome(s):
    return s == s[::-1] # daca s e egal cu inversul sau


# Driver code
ans = isPalindrome(number)

if ans:
    print("the number is palindrome")
else:
    print("number is not palindrome")
