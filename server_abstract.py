from flask import Flask

class CommendExecutor:
    def execute(self, commend: dict):
        raise NotImplementedError('execute must be implemented')


    def show_inventory(self):
        pass

    def show_one_category(self):
        pass

    def show_item_details(self):
        pass

    def change_price(self, commend: dict):
        raise NotImplementedError

    def add_item(self, commend: dict):
        raise NotImplementedError

    def remove_item(self, commend: dict):
        raise NotImplementedError

    def show_money_status(self):
        pass

    def deposit_money(self, commend: dict):
        raise NotImplementedError

    def withdraw_money(self, commend: dict):
        raise NotImplementedError




def create_app(executor):
    app = Flask(__name__)


    @app.get("/api/Category")
    def api_category():
        pass


    @app.get("/api/ShoeAll")
    def api_shoe_all():
        pass


    @app.get("/api/ItemDetail")
    def api_item_detail():
        pass


    @app.post('/api/ChangePrice')
    def api_change_price():
        pass


    @app.post('/api/AddItem')
    def api_add_item():
        pass


    @app.post('/api/RemoveItem')
    def api_remove_item():
        pass


    @app.get('/api/ShowMoneyStatus')
    def api_show_money_status():
        pass


    @app.post('/api/DepositMoney')
    def api_deposit_money():
        pass


    @app.post('/api/WithdrawMoney')
    def api_withdraw_money():
        pass

    return app
