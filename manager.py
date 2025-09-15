from abc import ABC, abstractmethod


class ManagerAbc(ABC):


    @abstractmethod
    def change_price(self, new_price):
        pass

    @abstractmethod
    def change_cost(self, new_cost):
        pass

    @abstractmethod
    def sale_item(self, item: Product, num: int=1):
        pass

    @abstractmethod
    def bay_item(self, item: Product, num: int=1):
        pass







