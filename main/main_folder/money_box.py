class MoneyBox:

    def __init__(self, capacity = 0): # вместимость копилки
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):  # True, если можно добавить v монет, False иначе
        if self.capacity >= self.count + v:
            return True
        else:
            return False

    def add(self, v): # положить v монет в копилку
        if self.can_add(v):
            self.count += v


box = MoneyBox(6)
print(box.count, box.capacity)
box.add(5)
print(box.count, box.capacity)
box.add(1)
print(box.count, box.capacity)
box.add(5)
print(box.count, box.capacity)