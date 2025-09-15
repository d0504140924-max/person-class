from abc import ABC, abstractmethod


class MoneyManagerAbc(ABC)


    @abstractmethod
    def add_money(self, amount, _from: str):
        pass

    @abstractmethod
    def withdraw(self, amount: int, _for: str, to: str=''):
        pass

    @abstractmethod
    def report(self):
        pass

    @abstractmethod
    def movements_record(self, type: str):

    @abstractmethod
    def month_report(self, month: int):
        pass
