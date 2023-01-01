import random
import math
freq = 0
N = 100000
for i in range(N):
    p1 = random.random()
    p2 = random.random()
    if math.fabs(p1-p2) <= 0.5:
        freq += 1
print(freq/N)