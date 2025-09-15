from abc import ABC, abstractmethod


class MoneyManagerAbc(ABC):


    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount: int):
        pass

    @abstractmethod
    def report(self):
        pass

    @abstractmethod
    def movements_record(self, type: str):
        pass

    @abstractmethod
    def month_report(self, month: int):
        pass
