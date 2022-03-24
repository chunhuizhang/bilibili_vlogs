
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


model = cp_model.CpModel()

base = 10

# SEND + MORE = MONEY
S = model.NewIntVar(1, base-1, 'S')
M = model.NewIntVar(1, base-1, 'M')

E = model.NewIntVar(0, base-1, 'E')
N = model.NewIntVar(0, base-1, 'N')
D = model.NewIntVar(0, base-1, 'D')
O = model.NewIntVar(0, base-1, 'O')
R = model.NewIntVar(0, base-1, 'R')
Y = model.NewIntVar(0, base-1, 'Y')

letters = [S, M, E, N, D, O, R, Y]

model.AddAllDifferent(letters)
model.Add(S*base**3 + E*base**2 + N*base + D
          + M*base**3 + O*base**2 + R*base + E
          == M*base**4 + O*base**3 + N*base**2 + E*base + Y)

solver = cp_model.CpSolver()
solution_printer = VarArraySolutionPrinter(letters)
solver.parameters.enumerate_all_solutions = True

solver.Solve(model, solution_printer)

# print(
#     f"  {solver.Value(S)}{solver.Value(E)}{solver.Value(N)}{solver.Value(D)}\n+ {solver.Value(M)}{solver.Value(O)}{solver.Value(R)}{solver.Value(E)}\n={solver.Value(M)}{solver.Value(O)}{solver.Value(N)}{solver.Value(E)}{solver.Value(Y)}")
