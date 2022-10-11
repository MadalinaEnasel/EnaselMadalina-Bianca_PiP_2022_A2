# Write a function that extract a number from a text (for example if the text is "An apple is 123 USD",
# this function will return 123, or if the text is "abc123abc" the function will extract 123). The
# function will extract only the first number that is found.

def number(string):
    nr=0
    for i in string:
        char = chr(i)
        if char.isdigit():
            while char.isdigit():
                nr = nr*10+int(char)
            break
    return nr
