def numbers(lst):

    new_lst = []
    for el in lst:
        if type(el) in [int, float, complex]:
            new_lst.append(el)
    return new_lst