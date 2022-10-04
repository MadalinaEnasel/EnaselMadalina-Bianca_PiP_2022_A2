#Write a script that receives two strings and prints the number of occurrences of the first string
# in the second.

s1 = input("tell me the first string")
s2 = input("now the second")

print (s2.count(s1))

# more accurate

results = 0
sub_len = len(s1)
for i in range(len(s2)):
    if s2[i:i+sub_len] == s1:
        results += 1
print(results)