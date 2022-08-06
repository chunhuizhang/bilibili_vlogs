

def monthly_analysis(p, r, n):
    r /= 12
    paied_p = 0
    for i in range(n):
        month_pay = p/n + (p - paied_p)*r
        print(i, month_pay, p/n, (p-paied_p)*r)
        paied_p += p/n


if __name__ == '__main__':

    p = 2000000
    r = 0.055
    n = 30*12
    monthly_analysis(p, r, n)
