

def generator():
    for i in range(10):
        yield i
    print(i)


def fun():
    for i in range(10):
        print(i)
    print(i)


if __name__ == '__main__':

    # for i in generator():
    #     print(i)
    fun()
