from abc import ABC, abstractmethod
class Inventory(ABC):

    @abstractmethod
    def get_amount(self, item):
        pass


    @abstractmethod
    def add_item(self, item, mun=None):
        pass


    @abstractmethod
    def remove_item(self, item, num=None):
        pass


    @abstractmethod
    def update_amount(self, item, new_amount):
        pass


    @abstractmethod
    def show_inventory(self):
        pass


