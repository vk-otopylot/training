class BankAcc:
    bank_name = 'State Bank of India'
    def __init__(self, acc_holder, acc_no, balance):
        self.acc_holder = acc_holder
        self._acc_no = acc_no
        self.__balance = balance

    def get_balance(self):
        return f'Your current balance: {self.__balance}'

    def set_balance(self, amount):
        self.__balance = amount
        return f'Your current balance: {self.__balance}'

ac1 = BankAcc('vivek kakadia', 12345678, 1200)
print(ac1.set_balance(7800))