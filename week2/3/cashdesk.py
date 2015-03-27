class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __int__(self):
        return int(self.amount)

    def __str__(self):
        return "A %s$ bill" % self.amount

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)


class BillBatch:

    def __init__(self, listbills):
        self.listbills = listbills

    def __len__(self):
        return len(self.listbills)

    def total(self):
        return sum(self.listbills)

    def __getitem__(self, index):
        return self.listbills[index]


class CashDesk:

    def __init__(self):
        self.desk = {}

    def take_money(self, money):
        if type(money) == Bill:
            if money in self.desk:
                self.desk[money] += 1
            else:
                self.desk[money] = 1
        elif type(money) == BillBatch:
            for bill in money:
                if bill in self.desk:
                    self.desk[bill] += 1
                else:
                    self.desk[bill] = 1

    def total(self):
        return "We have a total of %d in the desk" % sum([int(self.desk[key])*int(key) for key in self.desk.keys()])

    def inspect(self):
        print("We have the following count of bills, sorted in ascending order:")
        for key in self.desk.keys():
            print("{}$ bills - {}".format(key, self.desk[key]))
