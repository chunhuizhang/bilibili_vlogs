

def npv(pays, r):
    return sum([pay/((1+r)**(i+1)) for i, pay in enumerate(pays)])


if __name__ == '__main__':
    pays = [236.8, 236.8+1000]
    r = 0.2368
    print(npv(pays, r))

    pays = [192.06, 192.06+1100]
    r = 0.1746
    print(npv(pays, r))
