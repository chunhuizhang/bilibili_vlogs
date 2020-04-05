import random

import matplotlib.pyplot as plt

gates = ['coat', 'coat', 'car']


def not_change(N=1000):
    win = 0
    for i in range(N):
        random.shuffle(gates)
        # print(gates)
        chosed = random.randint(0, 2)
        print('chosed {}({})'.format(chosed, gates))
        unchosed_coat = random.choice([i for i in range(3) if i != chosed and gates[i] != 'car'])
        print('{} is a coat, change or not'.format(unchosed_coat))
        final_chose = chosed
        if gates[final_chose] == 'car':
            win += 1
            print('not change, win')
        else:
            print('not change, lose')
    return win


def change(N=1000):
    win = 0
    for i in range(N):
        random.shuffle(gates)
        # print(gates)
        chosed = random.randint(0, 2)
        print('chosed {}({})'.format(chosed, gates))
        unchosed_coat = random.choice([i for i in range(3) if i != chosed and gates[i] != 'car'])
        print('{} is a coat, change or not'.format(unchosed_coat))
        for i in range(3):
            if i != chosed and i != unchosed_coat:
                final_chose = i
        if gates[final_chose] == 'car':
            print('change, win')
            win += 1
        else:
            print('change, lose')
    return win


if __name__ == '__main__':
    # N = 100000
    # # print('not change, win {}/{}'.format(not_change(N), N))
    # print('change, win {}/{}'.format(change(N), N))

    not_change_rates = []
    change_rates = []

    for n in [10, 100, 1000, 10000, 100000, 100000]:
        not_change_rates.append(not_change(n) / n)
        change_rates.append(change(n) / n)

    plt.plot(range(6), not_change_rates, range(6), change_rates)
    plt.show()
