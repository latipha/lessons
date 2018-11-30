class MoneyBox:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        if v + self.count > self.capacity:
            return False
        else:
            return True

    def add(self, v):
        self.count += v


x = MoneyBox()
if x.can_add(3):
    x.add(3)

print(x.count)