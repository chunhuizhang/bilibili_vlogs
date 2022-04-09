from pyomo.environ import *

A = ['hammer', 'wrench', 'screwdriver', 'towel']
b = {'hammer': 8, 'wrench': 3, 'screwdriver': 6, 'towel': 11}
w = {'hammer': 5, 'wrench': 7, 'screwdriver': 4, 'towel': 3}

W_max = 14
model = ConcreteModel()
model.x = Var(A, within=Binary)

model.value = Objective(
    expr=sum(b[i] * model.x[i] for i in A), sense=maximize)
model.weight = Constraint(
    expr=sum(w[i] * model.x[i] * model.x[i] for i in A) <= W_max)
opt = SolverFactory('ipopt')
result_obj = opt.solve(model, tee=True)

model.pprint()