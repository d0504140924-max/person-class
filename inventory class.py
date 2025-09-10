from abc import ABC, abstractmethod
class Inventory(ABC):

    @abstractmethod
    def get_amount(self, item, amount):
        pass


    @abstractmethod
    def add_item(self, item):
        pass


    @abstractmethod
    def remove_item(self, item):
        pass


    @abstractmethod
    def update_amount(self, item, new_amount):
        pass


    @abstractmethod
    def existing_inventory(self):
        pass


