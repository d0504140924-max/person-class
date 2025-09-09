class Product:


    _product_id: str
    _category: str
    _product_name: str
    _manufacturer:str
    _price: float

    def __init__(self, product_id, category, product_name, manufacturer, price):
        self.product_id = product_id
        self.category = category
        self.product_name = product_name
        self.manufacturer = manufacturer
        self.price = price


    @property
    def product_id(self):
        return self._product_id
    @product_id.setter
    def product_id(self, new_id):
        assert isinstance(new_id, str)
        self.product_id = new_id


    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, new_category):
        assert isinstance(new_category, str)
        self.category = new_category


    @property
    def product_name(self):
        return self._product_name
    @product_name.setter
    def product_name(self, new_name):
        assert isinstance(new_name, str)
        self.product_name = new_name


    @property
    def manufacturer(self):
        return self._manufacturer
    @manufacturer.setter
    def manufacturer(self, new_manufacturer):
        assert isinstance(new_manufacturer, str)
        self.manufacturer = new_manufacturer


    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        assert isinstance(new_price, float)
        self.price = new_price


