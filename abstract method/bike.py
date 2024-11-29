from abc import ABC, abstractmethod
class RE(ABC):
    @abstractmethod
    def engine(self):
        pass
    def Gears(self):
        print('5 gears')

class Classic(RE):
    def engine(self):
        print('350CC')

class GT(RE):
    def engine(self):
        print('650CC')

class Himalayan(RE):
    def engine(self):
        print('452CC')

obj = Classic()
obj.engine()
obj.Gears()
obj1 = GT()
obj1.engine()
obj1.Gears()