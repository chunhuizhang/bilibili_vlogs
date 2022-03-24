
from abc import ABCMeta, abstractmethod


class Person(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def wear(self):
        print('着装: ')


class Engineer(Person):

    def __init__(self, name, skill):
        super().__init__(name)
        self._skill = skill

    def wear(self):
        print(f'我是 {self._name} 工程师, 我会 {self._skill}')
        super().wear()


class ClothingDecorator(Person):
    def __init__(self, person: Person):
        self._decoratored = person

    def wear(self):
        self._decoratored.wear()
        self.decorate()

    @abstractmethod
    def decorate(self):
        pass


class CasualPantDecorator(ClothingDecorator):
    def __init__(self, person: Person):
        super().__init__(person)
    def decorate(self):
        print('一条卡其色裤子')


class BeltDecorator(ClothingDecorator):
    def __init__(self, person: Person):
        super().__init__(person)

    def decorate(self):
        print('一条黑色腰带')

if __name__ == '__main__':
    tony = Engineer('Tony', '算法')
    pant = CasualPantDecorator(tony)
    belt = BeltDecorator(pant)
    belt.wear()



