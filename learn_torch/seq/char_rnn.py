
from io import open
import glob
import os
import unicodedata
import string


def find_files(path):
    return glob.glob(path)


def uni_to_ascii(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                    if unicodedata.category(c) != 'Mn' and c in all_letters)


def build_vocab(filepath):
    def read_lines(filename):
        lines = open(filename, encoding='utf-8').read().strip().split('\n')
        return [uni_to_ascii(line) for line in lines]

    category_lines = {}
    all_categories = []

    for filename in find_files(filepath):
        category = os.path.splitext(os.path.basename(filename))[0]
        lines = read_lines(filename)
        all_categories.append(category)
        category_lines[category] = lines
    return category_lines, all_categories



if __name__ == '__main__':
    all_letters = string.ascii_letters + " .,;'"
    n_letters = len(all_letters)
    print('n_letters = {}'.format(n_letters))
    category_lines, all_categories = build_vocab('../text_data/names/*.txt')
    print(all_categories)

