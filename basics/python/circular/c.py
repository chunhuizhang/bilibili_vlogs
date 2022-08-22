
from b import B
from a import A


a_inst = A()
b_inst = B()

print(a_inst.foo(b_inst))
b_inst.append(a_inst)
