

def monthly_analysis(p, r, n):
    r = r/12
    month_p_and_i = p*r*(1+r)**n/((1+r)**n - 1)
    remaining_p = p
    for i in range(n):
        month_i = remaining_p*r
        month_p = month_p_and_i - month_i
        remaining_p -= month_p
        print(i, month_p_and_i, month_p, month_i)


if __name__ == '__main__':
    p = 600000
    r = 0.06
    n = 20*12
    monthly_analysis(p, r, n)

