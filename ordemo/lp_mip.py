from ortools.linear_solver import pywraplp
import numpy as np


# solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)
# solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.GLPK_LINEAR_PROGRAMMING)
# solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.CLP_LINEAR_PROGRAMMING)
# solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
solver = pywraplp.Solver.CreateSolver('SCIP')


swordsmen = solver.IntVar(0, solver.infinity(), 'swordsmen')
bowmen = solver.IntVar(0, solver.infinity(), 'bowmen')
horsemen = solver.IntVar(0, solver.infinity(), 'horsemen')

x = np.asarray([swordsmen, bowmen, horsemen])
A = np.asarray([[60, 20, 0], [80, 10, 40], [140, 0, 100]])
b = np.asarray([1200, 800, 600])
c = np.asarray([70, 95, 230])

Ax = A.T.dot(x)
for i in range(len(b)):
    solver.Add(Ax[i] <= b[i])

solver.Maximize(np.inner(x, c))

status = solver.Solve()
# If an optimal solution has been found, print results
if status == pywraplp.Solver.OPTIMAL:
  print('================= Solution =================')
  print(f'Solved in {solver.wall_time():.2f} milliseconds in {solver.iterations()} iterations')
  print()
  print(f'Optimal power = {solver.Objective().Value()} 💪power')
  print('Army:')
  print(f' - 🗡️Swordsmen = {swordsmen.solution_value()}')
  print(f' - 🏹Bowmen = {bowmen.solution_value()}')
  print(f' - 🐎Horsemen = {horsemen.solution_value()}')
else:
  print('The solver could not find an optimal solution.')