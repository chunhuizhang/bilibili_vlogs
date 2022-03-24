
import numpy as np
from numpy.linalg import matrix_rank

if __name__ == '__main__':
    m = np.asarray([[1, 2, 3], [4, 5, 6], [5, 7, 9]])
    matrix_rank(m)