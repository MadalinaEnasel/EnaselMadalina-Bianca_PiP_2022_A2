def pereche_par_impar(lst1, lst2):

    def functie_1(lst_1, lst_2):
        return_list = []
        for item in list(zip(lst1, lst2)):

            a = item[1][1] - item[0][1]
            b = item[0][0] - item[1][0]
            c = a * item[0][0] + b * item[0][1]
            return_list.append(tuple((a, b, -c)))
        return return_list

    def functie_2(lst_1, lst_2):

        def get_coord(point_a, point_b):

            a = point_b[1] - point_a[1]
            b = point_a[0] - point_b[0]
            c = a * point_a[0] + b * point_a[1]

            return tuple((a, b, -c))

        return list(map(get_coord, lst1, lst2))

    result_zip = functie_1(lst1, lst2)
    result_map = functie_2(lst1, lst2)

    return result_zip, result_map