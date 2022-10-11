#Write a function that counts how many words exists in a text. A text is considered to be form out of
# words that are separated by only ONE space. For example: "I have Python exam" has 4 words.

string = input("give me a phrase")
result = " ".join(string.split())

result = result.count(" ")

print ("There are ", result+1, " words")