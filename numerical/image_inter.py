'''
    use bilinear interpolation to resize an image
    https://www.brezeale.com/?p=812
'''

import numpy as np
from PIL import Image


def resizeImage(name):
    img1 = Image.open(name)

    old = np.asarray(img1)  # convert to Numpy array
    rows, cols, layers = old.shape
    new = np.zeros((2 * rows - 1, 2 * cols - 1, layers))
    print("original dimensions:", old.shape)

    for layer in range(3):
        new[:, :, layer] = resizeLayer(old[:, :, layer])

    # convert the values to unsigned, 8-bit integers
    new = new.astype(np.uint8)
    print("     new dimensions:", new.shape)

    img2 = Image.fromarray(new)  # convert back to Image
    newName = "big-" + name
    img2.save(newName)


def resizeLayer(old):
    rows, cols = old.shape

    rNew = 2 * rows - 1
    cNew = 2 * cols - 1
    new = np.zeros((rNew, cNew))

    # move old points
    new[0:rNew:2, 0:cNew:2] = old[0:rows, 0:cols]

    ''' alternative approach
    # something like this would be necessary in languages
    #   that don't support slicing
    new = np.zeros( (2*rows - 1, 2*cols - 1) )
    for r in range(rows) :
        for c in range(cols) :
            new[2*r, 2*c] = old[r,c]

    rows, cols = new.shape
    '''

    # produce vertical values
    new[1:rNew:2, :] = (new[0:rNew - 1:2, :] + new[2:rNew:2, :]) / 2
    ''' alternative approach
    for r in range(1, rows, 2) :
        for c in range(0, cols, 2) :
            # top + bottom
            new[r,c] = ( new[r-1,c] + new[r+1,c] ) // 2
    '''

    # produce horizontal values
    new[:, 1:cNew:2] = (new[:, 0:cNew - 1:2] + new[:, 2:cNew:2]) / 2
    ''' alternative approach
    for r in range(0, rows, 2) :
        for c in range(1, cols, 2) :
            # left + right
            new[r,c] = ( new[r,c-1] + new[r,c+1] ) // 2
    '''

    # produce center values
    new[1:rNew:2, 1:cNew:2] = (new[0:rNew - 2:2, 0:cNew - 2:2] +
                               new[0:rNew - 2:2, 2:cNew:2] +
                               new[2:rNew:2, 0:cNew - 2:2] +
                               new[2:rNew:2, 2:cNew:2]) / 4
    ''' alternative approach
    for r in range(1, rows, 2) :
        for c in range(1, cols, 2) :
            # top + bottom + left + right
            new[r,c] = ( new[r-1,c] + new[r+1,c] + new[r,c-1] + new[r,c+1] ) // 4
    '''

    return new


####################  main  ####################

test = np.array([[10, 40], [30, 20]])
print(test)
test = resizeLayer(test)
print()
print(test)

# filename = 'book_fausett_small.jpg'
# resizeImage(filename)
