from datetime import datetime
from promotions import rebate_scheme
from orders import log


def create_id():
    pass


class Customer():
    def __init__(self, id=0, first_name=None, last_name=None, age=None, contact=None, address=None,
                 history=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.contact = contact
        self.address = address
        self.history = history  # example dict { 2020-10-02: "Liver purchased - 3",
                                                # 2020-10-12: "Bonus redeemed - heart 0, liver 2, lung 1"}

    def get_id(self):
        if self.id == 0:
            self.id = create_id()  # futuristic function to create id for new customer
        return self.id

    def get_firstname(self):
        return self.first_name

    def get_lastname(self):
        return self.last_name

    def get_history(self):
        if self.history is not None:
            return self.history

    def add_transaction(self, data):
        self.history.append(data)


class CustomerPromo(Customer):
    def __init__(self, promo_type=None, organ=None, cash=0, price=0, bonus_ratio=0):
        super().__init__()
        self.organ = organ
        self.cash = cash
        self.price = price
        self.bonus_ratio = bonus_ratio
        self.promo_type = promo_type
        self.bonus_to_receive = None

    def get_promo_results(self):
        try:
            if self.promo_type:
                possibles = globals().copy()
                possibles.update(locals())
                method = possibles.get(self.promo_type)
                if not method:
                    raise NotImplementedError("Method %s not implemented" % self.promo_type)
                self.bonus_to_receive = method(organ_to_purchase=self.organ, available_cash=self.cash,
                                               product_price=self.price, bonus_ratio=self.bonus_ratio)
                return
            else:
                print("please input the type of promotion")
        except NotImplementedError as e:
            print("Method %s not implemented" % self.promo_type)
            log.error(e)
        except Exception as err:
            print(err)
            log.error(err)
