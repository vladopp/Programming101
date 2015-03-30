class BankAccount:

    def __init__(self, name, amount, currency):
        if amount < 0:
            raise(ValueError)
        self.__name = str(name)
        self.__amount = amount
        self.__currency = str(currency)
        self.__history = ['Account was created']

    def getname(self):
        return self.__name

    def getamount(self):
        return self.__amount

    def getcurrency(self):
        return self.__currency

    def deposit(self, amount):
        if amount < 0:
            raise(ValueError)
        self.__amount += amount
        self.__history.append("Deposited {}{}".format(amount, self.getcurrency()))

    def balance(self):
        self.__history.append("Balance check -> {}{}".format(self.getamount(), self.getcurrency()))
        return self.getamount()

    def withdraw(self, amount):
        if amount < 0:
            raise(ValueError)
        if amount > self.getamount():
            self.__history.append('Withdraw for {}{} failed'.format(amount, self.getcurrency()))
            return False
        self.__history.append("{}{} was withdrawed".format(amount, self.getcurrency()))
        self.__amount -= amount
        return True

    def history(self):
        return self.__history

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.getname(), self.getamount(), self.getcurrency())

    def __int__(self):
        self.__history.append("__int__ check -> {}{}".format(self.getamount(), self.getcurrency()))
        return int(self.getamount())

    def transfer_to(self, other, value):
        if value < 0:
            raise(ValueError)
        if self.getcurrency() != other.getcurrency():
            return False
        if value <= self.getamount():
            self.__amount -= value
            self.__history.append('Transfer to {} for {}{}'.format(other.getname(), value, self.getcurrency()))
            other.__amount += value
            other.__history.append('Transfer from {} for {}{}'.format(self.getname(), value, self.getcurrency()))
            return True
        return False
