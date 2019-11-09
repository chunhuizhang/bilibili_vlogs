
import random
import matplotlib.pyplot as plt


denominator = 0
numerator = 0


results = []
for N in range(10000, 1000000, 10000):
    for i in range(N):

        b = random.random()     # 0-1
        a = random.random()     # 0-1

        if a < b:
            denominator += 1

            if a+(b-a) > 1-b and a+(1-b) > b-a and (b-a)+(1-b) > a:
                numerator += 1
    print(N, numerator*1./denominator)
    results.append(numerator*1./denominator)

# print(results)
plt.scatter(range(len(results)), results)
plt.show()
