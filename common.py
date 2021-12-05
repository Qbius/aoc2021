from re import search

class raw_input:
    pass

class RegexBase:
    pass

def regex(pattern, types):
    return type('', (RegexBase,), {'process': lambda lines: [[arg_type(arg) for arg, arg_type in zip(search(pattern, line).groups(), types)] for line in lines]})
