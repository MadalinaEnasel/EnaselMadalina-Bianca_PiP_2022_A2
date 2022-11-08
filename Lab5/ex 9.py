import ex7
import ex8

def suma_perechi(pairs):
    """
    :param pairs:
    :return:
    """
    return [{"sum": pair[0] + pair[1],
             "prod": pair[0]*pair[1],
             "pow": pair[0]**pair[1]} for pair in pairs]

def sum_digits(x):
        return sum(map(int, str(x)))

print(ex7.process(filters=[lambda item: item % 2 == 0,
                           lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
                  limit=2,
                  offset=2))

print(suma_perechi(pairs=[(5, 2), (19, 1), (30, 6), (2, 2)]))