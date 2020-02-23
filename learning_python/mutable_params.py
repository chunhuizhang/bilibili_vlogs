
def append_to(element, to=[]):
    to.append(element)
    return to


if __name__ == '__main__':

    my_list = append_to(12)
    print(my_list, append_to)

    my_other_list = append_to(42)
    print(my_other_list, append_to)
