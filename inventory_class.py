import json
import os
from inventory_abstract_class import InventoryManage
from product_class import Product


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
        self._inventory_path = new_path1


    @property
    def items_path(self):
        return self._items_path
    @items_path.setter
    def items_path(self, new_path2):
        assert isinstance(new_path2, str)
        self._items_path = new_path2

    @property
    def items(self):
        return self.load_from_file(self.items_path)

    @property
    def inventory(self):
        return self.load_from_file(self.inventory_path)

    def load_from_file(self, path):
        if os.path.exists(path):
            with open(path, 'r') as json_file:
                return json.load(json_file)
        else:
            with open(path, 'a+') as json_file:
                json.dump([], json_file)
            return json.load(json_file)


    def save_file_inventory(self):
        with open(self.inventory_path, 'w') as json_file:
            json.dump(self.inventory, json_file)


    def save_file_items(self):
        with open(self.items_path, 'w') as json_file:
            json.dump(self.items, json_file)

    def get_amount(self, id_item):
        amount = self.inventory[id_item.id]
        return amount


    def add_item(self, item: Product, num=1):
        if not item.id in self.inventory:
            self.inventory.append({item.id: num})
            self.save_file_inventory()
        if not item.__dict__ in self.items:
            self.items.append(item.__dict__)
            self.save_file_items()


    def remove_item(self, item: Product, num=1):
        if item.id in self.inventory:
            for it in range(len(self.inventory)):
                if self.inventory[it][item.id] > 0:
                    self.inventory.remove(self.inventory[it])
            self.save_file_inventory()
        if item.__dict__ in self.items:
            self.items.remove(item.__dict__)
            self.save_file_items()


    def update_amount(self, item: Product, new_amount):
        if item.id in self.inventory:
            self.inventory[item.id] = new_amount
            self.save_file_inventory()
        else:
            return 'no such id hes found'


    def show_inventory(self):
        return self.inventory, self.items







