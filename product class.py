class Product:


    _id: str
    _category: str
    _name: str
    _manufacturer:str
    _price: float
    _cost: float

    def __init__(self, product_id, category, product_name, manufacturer, price):
        self.id = product_id
        self.category = category
        self.name = product_name
        self.manufacturer = manufacturer
        self.price = price
        self.cost = cost


    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, new_id):
        assert isinstance(new_id, str)
        self.id = new_id


    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, new_category):
        assert isinstance(new_category, str)
        self.category = new_category


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        assert isinstance(new_name, str)
        self.name = new_name


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


    @property
    def cost(self):
        return self._cost
    @cost.setter
    def cost(self, new_cost):
        assert isinstance(new_cost, float)
        self.cost = new_cost


