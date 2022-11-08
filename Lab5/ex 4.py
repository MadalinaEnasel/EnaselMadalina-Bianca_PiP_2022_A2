def function4(*args, **kwargs):

    return_list = []

    for arg in args:
        if type(arg) == dict:
            if len(arg.keys()) >= 2 and any([True if type(key) == str and len(key) >= 3 else False
                                             for key in arg.keys()]):
                return_list.append(arg)

    for kw in kwargs.keys():
        if type(kwargs[kw]) == dict:
            if len(kwargs[kw].keys()) >= 2 and any([True if type(key) == str and len(key) >= 3 else False
                                             for key in kwargs[kw].keys()]):
                return_list.append(kwargs[kw])

    return return_list