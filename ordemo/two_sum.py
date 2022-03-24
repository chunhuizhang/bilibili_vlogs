from ortools.sat.python import cp_model


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


l = [2, 7, 1, 3, 6, 9, 10, -1, 12, 22]
target = 9

model = cp_model.CpModel()

xs = [model.NewBoolVar(str(i)) for i in range(len(l))]

model.Add(sum(xs) == 2)

model.Add(sum([xs[i]*l[i] for i in range(len(l))]) == target)
solver = cp_model.CpSolver()
solution_printer = VarArraySolutionPrinter(xs)
solver.parameters.enumerate_all_solutions = True
solver.Solve(model, solution_printer)

