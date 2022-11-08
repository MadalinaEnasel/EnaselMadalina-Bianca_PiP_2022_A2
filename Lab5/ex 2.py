def suma(*args, **kwargs):

    sum = 0

    for kw in kwargs.keys():
        sum += int(kwargs[kw])

    return sum


anonim_suma = lambda *args, **kwargs: sum([val for val in kwargs.values()])

