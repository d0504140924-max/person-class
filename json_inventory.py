import json
import os
from inventory_abstracts import InventoryManage
from product import Product


class TheInventory(InventoryManage):

    _inventory_path: str
    _items_path: str


    def __init__(self, inventory_path, items_path):
        self.inventory_path = inventory_path
        self.items_path = items_path




    @property
    def inventory_path(self):
        return self._inventory_path
    @inventory_path.setter
    def inventory_path(self, new_path1):
        assert isinstance(new_path1, str)
        assert os.path.exists(new_path1)
        self._inventory_path = new_path1


    @property
    def items_path(self):
        return self._items_path
    @items_path.setter
    def items_path(self, new_path2):
        assert isinstance(new_path2, str)
        assert os.path.exists(new_path2)
        self._items_path = new_path2

    @property
    def items(self):
        return self.load_from_file(self.items_path)

    @property
    def inventory(self):
        return self.load_from_file(self.inventory_path)


    @staticmethod
    def load_from_file(path):
        with open(path, 'r') as json_file:
            return json.load(json_file)


    @staticmethod
    def save_file(path, value):
        with open(path, 'w') as json_file:
            json.dump(value, json_file)


    def get_amount(self, id_item):
        for i in self.inventory:
            if id_item.id in i:
                return id_item, i[id_item.id]
        return 0


    def add_item(self, item: Product, num=1):
        if not item in self.inventory:
            data = self.inventory
            data.append({item.id:num})
            self.save_file(self.inventory_path, data)
        if not item in self.items:
            data = self.items
            data.append(item.__dict__)
            self.save_file(self.items_path, data)


    def remove_item(self, item: Product, num=1):
        if item in self.inventory:
                data = self.inventory
                data.remove(item)
                self.save_file(self.inventory_path, data)
        if item in self.items:
            data = self.items
            data.remove(item.__dict__)
            self.save_file(self.items_path, data)


    def update_amount(self, item: Product, new_amount):
        data = self.inventory
        for i in data:
            if item.id in i:
                i[item.id] = new_amount
                self.save_file(self.inventory_path, data)
            else:
                return 'no such id hes found'
        return 0


    def show_inventory(self):
        return self.inventory, self.items







