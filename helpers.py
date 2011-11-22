
import re
import string
from errors import *
from itertools import product

__all__ = ['split_space_key', 'default_gameboard', 'generate_range', 
    'convert_space_key', 'replace_chars']

def split_space_key(space):
    try:
        return list(re.findall('([a-z]+)([0-9]+)', space))[0]
    except IndexError:
        raise InvalidSpace()

def convert_space_key(space, cols=10, rows=10):
    a, b = split_space_key(space)
    b = int(b) - 1
    try:
        n = string.lowercase.index(a) + (b * cols)
    except ValueError:
        raise SpaceOutOfBounds(space)
    if n > (cols * rows) -1:
        raise SpaceOutOfBounds(space)
    return n

def default_gameboard(cols=10, rows=10):
    return ''.join([''.join(['n' for _ in range(cols)]) for _ in range(rows)])

def generate_range(start, end):
    salpha, snum = split_space_key(start)
    ealpha, enum = split_space_key(end)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    if salpha != ealpha and snum != enum:
        raise CannotPlaceDiagonally()
    elif salpha == ealpha:
        return [salpha + str(a) for a in range(int(snum), int(enum)+1)]
    else:
        s = letters.index(salpha)
        e = letters.index(ealpha) + 1
        return [a + snum for a in letters[s:e]]

def replace_chars_gen(indexes, replacement, subject):
    """the replacement generator"""
    for index, char in enumerate(subject):
        if index in indexes:
            yield replacement
        else:
            yield char

def replace_chars(indexes, replacement, subject):
    """replace the characters at the given indexes with the replacement character"""
    return ''.join(replace_chars_gen(indexes, replacement, subject))

