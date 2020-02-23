
def create_multipliers():
    return [lambda x : i * x for i in range(5)]


def create_multipliers_explicit():
    return [lambda x, i=i: i * x for i in range(5)]


def create_multipliers_yield():
    for i in range(5):
        yield lambda x: i*x


for multiplier in create_multipliers():
    print(multiplier.__closure__[0].cell_contents, multiplier(2))

for multiplier in create_multipliers_explicit():
    print(multiplier.__closure__, multiplier(2))

for multiplier in create_multipliers_yield():
    print(multiplier.__closure__[0].cell_contents, multiplier(2))

