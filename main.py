class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    def set_age(self, value):
        if value < 0:
            return False
        self._age = value
        return True

p = Person("Sara", 20)
print(p.set_age(-1))  # False
print(p.set_age(21))  # True
print(p.age)          # 21
