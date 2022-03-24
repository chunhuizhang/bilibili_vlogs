
import numpy as np
import matplotlib.pyplot as plt


batch = np.zeros([2, 3, 3, 3])
batch[0, :, :, 0] = np.asarray([[2.4, 0.3, 5.6],
                                [7.2, 0.0, 2.1],
                                [1.9, 7.4, 4.1]])
batch[0, :, :, 1] = np.asarray([[1.0, 2.1, 3.8],
                                [9.6, 2.0, 4.4],
                                [9.3, 3.9, 1.4]])
batch[0, :, :, 2] = np.asarray([[2.6, 8.1, 9.0],
                                [2.2, 6.6, 0.2],
                                [6.3, 6.0, 0.1]])

batch[1, :, :, 0] = np.asarray([[5.1, 9.0, 6.9],
                                [9.7, 2.9, 2.4],
                                [6.2, 0.7, 4.3]])
batch[1, :, :, 1] = np.asarray([[3.3, 7.9, 4.8],
                                [3.7, 2.0, 9.4],
                                [4.9, 2.1, 7.8]])

batch[1, :, :, 2] = np.asarray([[2.8, 5.4, 0.0],
                                [6.4, 1.8, 6.8],
                                [3.7, 5.6, 5.6]])
print(batch[:, :, :, 0].mean())
print(batch[:, :, :, 0].var())