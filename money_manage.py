from abc import ABC, abstractmethod



class MoneyManagerAbc(ABC):


    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount: int):
        pass

    @abstractmethod
    def current_amount(self):
        pass

    @abstractmethod
    def movements_record(self, type: str, start, end):
        pass

    @abstractmethod
    def month_report(self, month: int):
        pass
