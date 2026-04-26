class Customer:
    first_name: str
    last_name: str
    age: int
    email_address: str
    accounts_list: list

    def __init__(self, first_name, last_name, age, email_address, accounts_list):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email_address = email_address
        self.accounts_list = accounts_list


class Account:
    Account_number: int
    Account_Type: str
    balance: float
    transaction_history: list

    def __init__(self, Account_number, Account_Type, balance, transaction_history):
        self.Account_number = Account_number
        self.Account_Type = Account_Type
        self.balance = balance
        self.transaction_history = transaction_history

    # methods

    # deposit
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("deposit amount should be greater than zero")

        self.balance = self.balance + amount
        transaction = Transaction("deposit", amount, self.balance)
        self.transaction_history.append(transaction)

    # withdraw
    def withdraw(self, amount: float):
        if self.balance == 0:
            return "your available balance is zero"

        if amount <= 0:
            raise ValueError("withdraw amount should be greater than zero")

        if amount > self.balance:
            raise ValueError("account balance is lower than the amount you tried to withdraw")
        else:
            self.balance = self.balance - amount
            transaction = Transaction("withdraw", amount, self.balance)
            self.transaction_history.append(transaction)

    # transfer
    def transfer(self, target, amount: float):
        if target is None:
            raise ValueError("target account does not exist")

        if target == self:
            raise ValueError("source and target account cannot be same")

        if amount <= 0:
            raise ValueError("transfer amount should be greater than zero")

        if amount > self.balance:
            raise ValueError("account balance is lower than the amount you tried to transfer")

        self.balance = self.balance - amount
        target.balance = target.balance + amount

        source_transaction = Transaction("transfer_sent", amount, self.balance)
        target_transaction = Transaction("transfer_received", amount, target.balance)

        self.transaction_history.append(source_transaction)
        target.transaction_history.append(target_transaction)

    # print_statement
    def summary(self):
        print("Account Number:", self.Account_number)
        print("Account Type:", self.Account_Type)
        print("Balance:", self.balance)
        print("Transaction History:")

        if len(self.transaction_history) == 0:
            print("No transactions yet")
        else:
            for transaction in self.transaction_history:
                print(
                    transaction.transaction_type,
                    "| amount =", transaction.amount,
                    "| balance =", transaction.balance_after_transaction
                )


class Transaction:
    transaction_type: str
    amount: float
    balance_after_transaction: float

    def __init__(self, transaction_type, amount, balance_after_transaction):
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance_after_transaction = balance_after_transaction


if __name__ == "__main__":
    accounts_list = []
    check_transaction_history = []
    sav_transaction_history = []

    cust1 = Customer("Akshith", "Macharla", 25, "amacharla@csuchico.edu", accounts_list)

    check = Account(1024, "checking", 100.0, check_transaction_history)
    sav = Account(256, "savings", 500.0, sav_transaction_history)

    cust1.accounts_list.append(check)
    cust1.accounts_list.append(sav)

    check.deposit(50.0)
    sav.withdraw(100.0)
    check.transfer(sav, 25.0)

    print(cust1.first_name)
    print(cust1.accounts_list[0].Account_Type, cust1.accounts_list[0].balance)
    print(cust1.accounts_list[1].Account_Type, cust1.accounts_list[1].balance)

    check.summary()
    sav.summary()