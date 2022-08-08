
import copy

def check_num_id(i):
    a = i
    b = i
    print(i, id(a), id(b))


if __name__ == '__main__':
    for i in range(200, 260):
        check_num_id(i)
    copy.deepcopy()
