def vowel(string):

    return [ch for ch in string if ch.lower() in "aeiou"]


def vowels(string):

    anon_function = lambda string: [ch for ch in string if ch.lower() in "aeiou"]

    lista_1 = vowel(string)

    lista_2 = anon_function(string)

    filter = lambda string: list(filter(lambda x: x.lower() in "aeiou", string))

    list_3 = filter(string)

    return lista_1,lista_2,list_3