# 3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b,
# a reunited with b, a - b, b - a)
def intersection(a, b):
    return a.intersection(b)


def reunion(a, b):
    final_list = list(set(a) | set(b))
    return final_list


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 2, 3, 4, 34, 343, 54]
