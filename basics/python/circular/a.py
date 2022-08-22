

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from b import B


class A:
    def foo(self, b: 'B'):
        return 2*b.foo()

    def t(self):
        print('A.t()')
