

# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
from a import A


class B:

    def __init__(self):
        self.a_items = []

    def append(self, a: 'A'):
        a.t()
        self.a_items.append(a)

    def foo(self):
        return 5

