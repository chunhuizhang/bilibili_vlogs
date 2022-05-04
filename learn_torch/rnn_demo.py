from io import open
import glob
import os

import unicodedata
import string


all_letters = string.ascii_letters + " .,;'"
n_letters = len(all_letters)


def findFiles(path): return glob.glob(path)

def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in all_letters
    )

print(unicodeToAscii('Ślusàrski'))


print(findFiles('text_data/names/*.txt'))
