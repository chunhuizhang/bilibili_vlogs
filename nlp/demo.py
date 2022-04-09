from scipy.optimize import minimize, LinearConstraint
import numpy as np


def test1():
    fun = lambda x: x**2 + 2*x - 3
    x0 = np.asarray(1)
    res = minimize(fun, x0, bounds=[[0, None]], )
    print(res)


def test2():
    fun = lambda x: (x[0]-2)**2 + 4*(x[1]-1)**2
    x0 = [0, 0]
    cons = ({'type': 'ineq', 'fun': lambda x: 2 - x[0] - 2*x[1]})
    res = minimize(fun, np.asarray(x0),
                   method='slsqp',
                   constraints=cons, options={'disp': True})
    print(res)


def test3():
    fun = lambda x: -x[0]**2*x[1]
    x0 = np.asarray([0, 0])
    cons = ({'type': 'eq', 'fun': lambda x: x[0]**2+x[1]**2-1})
    res = minimize(fun, x0, constraints=cons, options={'disp': True})
    print(res)


if __name__ == '__main__':
    test2()
