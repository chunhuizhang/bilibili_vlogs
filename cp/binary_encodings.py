
from ortools.sat.python import cp_model


# https://developers.google.com/optimization/cp/cryptarithmetic

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count


def imply(x, y):
    # x=> y
    # not(x) or y
    # 0, 0/1
    # 1, 1

    # 1, 0
    # 0 or 0 = 0 false
    model.AddBoolOr([x.Not(), y])


def imply_2(x, y):
    # x => y
    model.AddImplication(x, y)


def two_way_imply(x, y):
    # x <=> y
    # x == y
    imply_2(x, y)
    imply_2(y, x)


def xor(x, y):
    # x or y
    model.AddBoolOr([x, y])
    # not (x and y) <=> not(x) or not(y)
    model.AddBoolOr([x.Not(), y.Not()])


if __name__ == '__main__':

    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    x = model.NewBoolVar('x')
    y = model.NewBoolVar('y')
    solution_printer = VarArraySolutionPrinter([x, y])
    solver.parameters.enumerate_all_solutions = True

    # imply
    # imply_2(x, y)
    # two_way_imply(x, y)
    xor(x, y)
    solver.Solve(model, solution_printer)
