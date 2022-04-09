from scipy import optimize
from scipy.spatial import distance

from ortools.sat.python import cp_model


def obj(x1, x2):
    return -(3*x1 + 4*x2)


if __name__ == '__main__':

    # 原始问题
    c = [-3, -4]
    A = [[1/2, 2], [3, 1]]
    b = [30, 25]

    res = optimize.linprog(c, A_ub=A, b_ub=b, bounds=[[0, None], [0, None]])
    print(res)

    print('=============')

    c = [30, 25]
    A = [[-1/2, -3], [-2, -1]]
    b = [-3, -4]
    res = optimize.linprog(c, A_ub=A, b_ub=b, bounds=[[0, None], [0, None]])
    print(res)
    print('=============')

    c = [5, 1]
    A = [[-2, -1], [-1, -1], [-2, -20]]
    b = [-6, -4, -21]
    res = optimize.linprog(c, A_ub=A, b_ub=b, bounds=[[0, None], [0, None]])
    print(res)
    print('=============')

    c = [-3, -5]
    A = [[1, 3], [3, 4]]
    b = [60, 120]
    res = optimize.linprog(c, A_ub=A, b_ub=b, bounds=[[10, None], [0, None]])
    print(res)
    print('=============')

    model = cp_model.CpModel()
    model.AddBoolOr()
