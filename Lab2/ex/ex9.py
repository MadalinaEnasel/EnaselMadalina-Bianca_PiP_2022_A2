#Write a functions that determine the most common letter in a string. For example if the string is
# "an apple is not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z)
# are to be considered. Casing should not be considered "A" and "a" represent the same character.

test_str = input("What string do you wanna check?")

print("The original string is : " + test_str)

all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = max(all_freq, key=all_freq.get)
print ("The maximum of all characters in GeeksforGeeks is : " + str(res))