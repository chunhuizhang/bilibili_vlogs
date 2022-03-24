
from datetime import datetime

class Test:
    alias = 'wudaokou nash'

    @staticmethod
    def static_mode(language):
        print(f'static method, {Test.alias} codes in {language}')

    @classmethod
    def class_mode(cls, language):
        print(f'class method, {cls.alias} codes in {language}')


class Repr:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__class__.__module__}.{self.__class__.__qualname__}(name={self.name})'

    def __str__(self):
        return f'{self.name}'


if __name__ == '__main__':
    t = Test()
    t.static_mode('chinese')
    t.class_mode('english')

    r = Repr('zhang')
    print(r)
    print(repr(r))
    print(str(r))

    now = datetime.now()
    print(now.__str__())
    print(now.__repr__())


