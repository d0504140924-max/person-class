import unittest
import json
import os

from list_of_products_class import TheInventory
from product_class import Product
from inventory_abstract_class import InventoryManage


class InventoryTest(unittest.TestCase):

    def setUp(self):
        self.inventory_file = 'inventory.json'
        self.items_file = 'items.json'
        with open(self.inventory_file, 'w') as f:
            json.dump([], f)
        with open(self.items_file, 'w') as f:
            json.dump([], f)

        self.the_inv = TheInventory(self.inventory_file, self.items_file)
        self.product_test = Product('2547', 'clothes', 'shirt', 'ZARA', 60.0, 37.0)


    def tearDown(self):
        if os.path.exists(self.inventory_file):
            os.remove(self.inventory_file)
        if os.path.exists(self.items_file):
            os.remove(self.items_file)


    def test_add_item(self):
        self.the_inv.add_item(self.product_test, num=1)
        data_file1 = self.the_inv.inventory
        self.assertTrue(any(i.get('id') == '2547' for i in data_file1))
        data_file2 = self.the_inv.items
        self.assertTrue(any(ii.get('name') == 'shirt' for ii in data_file2))


    def test_remove_item(self):
        self.the_inv.remove_item(self.product_test, num=1)
        data_file1 = self.the_inv.inventory
        self.assertFalse(any(i.get('id') == '2547' for i in data_file1))
        data_file2 = self.the_inv.items
        self.assertFalse(any(ii.get('name') == 'shirt' for ii in data_file2))


    def test_get_amount(self):
        self.the_inv.add_item(self.product_test, num=4)
        amount = self.the_inv.get_amount(self.product_test)
        self.assertEqual(amount, 3)


    def test_update_amount(self):
        self.the_inv.add_item(self.product_test, num=4)
        self.the_inv.update_amount(self.product_test, 10)
        amount = self.the_inv.get_amount(self.product_test)
        self.assertEqual(amount, 10)

if __name__ == '__main__':
    unittest.main()