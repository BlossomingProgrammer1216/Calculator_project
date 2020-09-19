class percent:
    def __init__(self, percent, object):
        self.percent = percent
        self.object = object

    def find_percent(percent, object):
        p = percent / 100
        rnd = round(object, 45)
        p_of = p * rnd
        print(f"{percent} percent of {object} is {p_of}")

class add:
    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2

    def adding(f1, f2):
        sum = f1 + f2
        print(f"{f1} + {f2} = {sum}")
class subtract:
    def __init__(self, o1, o2):
        self.o1 = o1
        self.o2 = o2

    def s(o1, o2):
        su = o1 - o2
        print(f"{o1} - {o2} = {su}")

class multiply:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def mult(m1, m2):
        m = m1 * m2
        print(f"{m1} * {m2} = {m}")

class divide:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
    def d(d1, d2):
        div = d1 / d2
        print(f"{d1} divided by {d2} is {div}")

class exponent:
    def __init__(self, number, power):
        self.number = number
        self.power = power
    def exp(number, power):
        exp = number * number * power
        print(f"{number} to the power of {power} is {exp}")