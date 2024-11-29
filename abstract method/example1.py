from abc import ABC, abstractmethod
class Parent(ABC):
    @abstractmethod
    def M1(self):
        pass

class Child1(Parent):
    def M1(self):
       pass        #implementations

class Child2(Parent):
    def M1(self):
        pass        #implementations