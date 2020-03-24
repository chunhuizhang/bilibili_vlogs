


def lexicoal_permute(seq):

    n = len(seq)
    max_x = -1
    seq.sort()
    print(seq)
    while True:
        for i in range(n-1):
            if seq[i] < seq[i+1]:
                max_x = i
        if max_x == -1:
            break
        max_y = -1
        for i in range(n):
            if seq[i] > seq[max_x]:
                max_y = i
        # swap
        seq[max_x], seq[max_y] = seq[max_y], seq[max_x]
        # reverse
        seq[max_x+1:] = seq[n-1:max_x:-1]
        max_x = -1
        print(seq)


if __name__ == '__main__':
    lexicoal_permute(['a', 'c', 'b'])
