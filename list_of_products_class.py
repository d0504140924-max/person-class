import json
import os
from inventory_class import Inventory
from product_class import Product


class Gson(Inventory):

    _path: str

    def __init__(self, path,):
        self.path = path
        self.items = self.load_from_file()

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, new_path):
        self._path = new_path





    def load_from_file(self):
        if os.path.exists(self.path):
            with open(self.path, 'r') as json_file:
                return json.load(json_file)
        return []


    def add_item(self, item: Product, mun=1):
        self.items.append(item.__dict__)
        self.save_file()


    def remove_item(self, item: Product, mun=1):
        self.items.remove(item.__dict__)
        self.save_file()


    def get_amount(self, item: Product):
        for it in self.items:
            if it['item'] == item:
                return it['amount']
        self.save_file()
        return None


    def update_amount(self, item: Product, new_amount):
        for it in self.items:
            if it['item'] == item:
                it['amount'] = new_amount
        self.save_file()


    def show_inventory(self):
        print(self.items)


    def save_file(self):
        with open(self.path, 'w') as json_file:
            json.dump(self.items, json_file)

