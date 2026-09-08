class Wallet:
    user_name: str
    wallet_balance: int
    payment_methods: list
    transaction_history: list

    def __init__(self, user_name, wallet_balance, payment_methods=None, transaction_history=None):
        self.user_name = user_name
        self.wallet_balance = wallet_balance
        self.payment_methods = [] if payment_methods is None else payment_methods
        self.transaction_history = [] if transaction_history is None else transaction_history

    def print_wallet_balance(self):
        print(self.wallet_balance)

    def add_payment_method(self, payment_method_obj):
        self.payment_methods.append(payment_method_obj)

    def list_payment_methods(self):
        for i in self.payment_methods:
            print(i)

    def recent_transaction_history(self):
        if len(self.transaction_history) > 0:
            return self.transaction_history[-1]
        else:
            return "you haven't made any transactions yet"

    def check_transaction_eligibility(self, amount):
        if amount <= 0:
            return False

        if amount <= self.wallet_balance:
            return True
        else:
            return False

    def deduct_balance(self, amount):
        if amount <= 0:
            return False

        if amount <= self.wallet_balance:
            self.wallet_balance -= amount
            return True
        else:
            return False

    def transaction_history_new(self, temp: str):
        self.transaction_history.append(temp)


class payment_method:
    def can_pay(self, amount):
        raise NotImplementedError("child class should implement can_pay")

    def __str__(self):
        return "payment method"


class UPIpaymentmethod(payment_method):
    upi_id: str
    active_status: bool

    def __init__(self, upi_id, active_status):
        self.upi_id = upi_id
        self.active_status = active_status

    def can_pay(self, amount):
        if amount <= 0:
            return False

        if self.active_status == True and self.upi_id != "":
            return True
        else:
            return False

    def __str__(self):
        return "UPI: " + self.upi_id


class Cardpaymentmethod(payment_method):
    lastfourdigitsofcard: int
    active_status: bool
    card_limit: int

    def __init__(self, lastfourdigitsofcard, active_status, card_limit):
        self.lastfourdigitsofcard = lastfourdigitsofcard
        self.active_status = active_status
        self.card_limit = card_limit

    def can_pay(self, amount):
        if amount <= 0:
            return False

        if self.active_status == True and amount <= self.card_limit:
            return True
        else:
            return False

    def __str__(self):
        return "Card ending with " + str(self.lastfourdigitsofcard)


class PaymentService:
    obj1: payment_method
    obj2: Wallet

    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2

    def service(self, amount):
        if amount <= 0:
            self.obj2.transaction_history_new("Payment failed: invalid amount")
            return "payment failed: invalid amount"

        if self.obj1.can_pay(amount) == False:
            self.obj2.transaction_history_new("Payment failed: payment method cannot be used")
            return "payment failed: payment method cannot be used"

        if self.obj2.deduct_balance(amount) == False:
            self.obj2.transaction_history_new("Payment failed: not enough wallet balance")
            return "payment failed: not enough wallet balance"

        self.obj2.transaction_history_new("Payment successful")
        return "payment successful"


wallet = Wallet("Akshith", 100)

upi = UPIpaymentmethod("akshith@upi", True)
card = Cardpaymentmethod(1234, True, 50)

wallet.add_payment_method(upi)
wallet.add_payment_method(card)

wallet.list_payment_methods()

service1 = PaymentService(upi, wallet)
print(service1.service(30))

wallet.print_wallet_balance()
print(wallet.recent_transaction_history())

service2 = PaymentService(card, wallet)
print(service2.service(60))

wallet.print_wallet_balance()
print(wallet.recent_transaction_history())