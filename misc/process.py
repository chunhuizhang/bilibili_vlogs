
from datetime import datetime

def merge():
    chinese = open('./raw_chinese.txt', encoding='UTF-8').readlines()
    english = open('./raw_english.txt', encoding='UTF-8').readlines()
    merge = open('./merge_{}.txt'.format(today), 'w', encoding='UTF-8')
    for c_row, e_row in zip(chinese, english):
        c_row = c_row.replace(',', ' ').replace('，', ' ')
        merge.write(' '.join(c_row.split()) + '\n')
        # e_row = e_row.replace(',', ' ').replace('，', ' ')
        merge.write(e_row)

def split():
    merge = open('./merge_{}.txt'.format(today), encoding='utf-8').readlines()
    chinese = open('./chinese_{}.txt'.format(today), 'w', encoding='utf-8')
    english = open('./english_{}.txt'.format(today), 'w', encoding='utf-8')
    for i, row in enumerate(merge):
        if i % 2 == 0:
            chinese.write(row)
        else:
            english.write(row)

if __name__ == '__main__':
    today = datetime.now().strftime('%Y%m%d')
    # merge()
    split()
    pass

