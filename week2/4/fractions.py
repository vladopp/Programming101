class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        for i in range(1, self.numerator+1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                self.numerator //= i
                self.denominator //= i

    def __str__(self):
        if self.numerator % self.denominator != 0:
            return "{} / {}".format(self.numerator, self.denominator)
        return str(self.numerator//self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator*other.denominator)

    def __sub__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)
        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator, self.denominator*other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __eq__(self, other):
        return self.numerator / self.denominator - other.numerator / other.denominator <= 10 ** (-12)
