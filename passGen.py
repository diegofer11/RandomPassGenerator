from random import choice, choices
from string import ascii_letters, digits


def new_pass(paswlength):
    """Function that generates random password based on user given length."""
    special = '#$%&()*+<=>?@_'
    lists = [ascii_letters, digits, special]
    pasw = ''.join(choice(choices(lists)[0]) for i in range(paswlength))
    return pasw
