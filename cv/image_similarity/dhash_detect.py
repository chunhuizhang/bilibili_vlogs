

from PIL import Image
import numpy as np
import imagehash


def image_to_dhash(image_path, hash_size=8):
    image = Image.open(image_path)
    # grey, resize: 9*8
    image = image.convert('L').resize((hash_size+1, hash_size), Image.ANTIALIAS)
    pixels = np.asarray(image)
    diff = pixels[:, 1:] > pixels[:, :-1]
    # dhash = sum(2**(i%8) for i, v in enumerate(diff.flatten()) if v)
    return diff

# def image_to_phash():


def binary_to_hex(arr):
    bit_str = ''.join(str(b) for b in 1*arr.flatten())
    print(bit_str)
    width = int(np.ceil(len(bit_str)/4))
    return '{:0>{width}x}'.format(int(bit_str, 2), width=width)


def hamming_distance(dhash1, dhash2, f=64):
    if isinstance(dhash1, str):
        dhash1 = int(dhash1, base=16)
    if isinstance(dhash2, str):
        dhash2 = int(dhash2, base=16)
    x = (dhash1 ^ dhash2) & ((1 << f) - 1)
    # 数1的个数
    ans = 0
    while x:
        ans += 1
        x &= x-1
    return ans


def hamming_dist(dhash1, dhash2):
    difference = (int(dhash1, 16)) ^ (int(dhash2, 16))
    return bin(difference).count("1")


def hash_functions_eval(hash_function=imagehash.dhash):
    lena_1 = hash_function(Image.open('./imgs/lena/origin-lena.png'))
    lena_2 = hash_function(Image.open('./imgs/lena/blur-lena.png'))
    lena_3 = hash_function(Image.open('./imgs/lena/resize-lena.png'))
    lena_4 = hash_function(Image.open('./imgs/lena/shift-lena.png'))
    forest = hash_function(Image.open('./imgs/forest-high.jpg'))

    hashs = [lena_1, lena_2, lena_3, lena_4, forest]
    for i in range(len(hashs)):
        for j in range(i + 1, len(hashs)):
            print(hash_function.__name__, i, j, hashs[i] - hashs[j])


def rotate_eval(img_path='./imgs/lena/origin-lena.png', hash_function=imagehash.dhash):
    origin_image = Image.open(img_path)
    origin_hash = hash_function(origin_image)
    for r in range(1, 180, 10):
        rotate_hash = hash_function(origin_image.rotate(r))
        print(hash_function.__name__, r, origin_hash - rotate_hash)


if __name__ == '__main__':
    # hash_functions_eval(imagehash.average_hash)
    # print('----------------------')
    #
    # hash_functions_eval(imagehash.phash)
    # print('----------------------')
    #
    # hash_functions_eval(imagehash.dhash)
    # print('----------------------')
    #
    # hash_functions_eval(imagehash.whash)

    rotate_eval(hash_function=imagehash.phash)

class Solution:
    def str_to_hex(self, s):
        return ''.join([hex(ord(c)).replace('0x', '') for c in s])
    def toHexspeak(self, num: str) -> str:
        h = self.str_to_hex(num)
        h = h.replace('1', 'I').replace('0', 'O')
        s = '23456789'
        for c in s:
            if c in h:
                return "ERROR"
        return h
Solution().toHexspeak("257")
