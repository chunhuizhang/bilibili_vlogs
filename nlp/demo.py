from scipy.optimize import minimize, LinearConstraint, rosen, rosen_der, rosen_hess
import numpy as np
import matplotlib.pyplot as plt


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


def example_16_4():
    func = lambda x: (x[0]-1)**2 + (x[1] - 2.5)**2
    x0 = np.asarray([0, 0])

    # bounds = np.asarray([[0, None],
    #                      [0, None]])

    cons = ({'type': 'ineq', 'fun': lambda x: x[0] - 2*x[1] + 2},
            {'type': 'ineq', 'fun': lambda x: -x[0] - 2*x[1] + 6},
            {'type': 'ineq', 'fun': lambda x: -x[0] + 2*x[1] + 2},
            {'type': 'ineq', 'fun': lambda x: x[0]},
            {'type': 'ineq', 'fun': lambda x: x[1]})

    res = minimize(func, x0,
                   # bounds=bounds,
                   constraints=cons,
                   jac=lambda x: np.asarray([2*(x[0]-1), 2*(x[1] - 2.5)]),
                   # hess=lambda x: np.asarray([[2, 0], [0, 2]]),
                   method='SLSQP')
    print(res)


if __name__ == '__main__':
    example_16_4()

