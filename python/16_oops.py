"""
# The four pillars:
#   Encapsulation - who is allowed to see or change.
                    Public: Anyone can see it. Anyone can change it.
                    Protected: Only the class itself and its "children" (subclasses) should use it.
                    Private: Only the class itself can see or change it.
#   Inheritance   - extends base class & use base class methods and attributes.
#   Polymorphism  - different classes use the exact same method name.
#   Abstraction   - a master blueprint, what should be must have implemented.
"""

# CLASS & OBJECT

class Mathematics:
    # CONSTRUCTOR
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self, b):
        return self.a - b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

maths_01 = Mathematics(3, 2)
print(maths_01.addition())
print(maths_01.subtraction(10))
print(maths_01.multiplication())
print(maths_01.division())

class Person:
    PI = 3.14

    def __init__(self, username): # constructor
       self.username = username

    def qwerty(self, age):
        print(f"Hello {self.username}, next year you'll turn to {age}!")

p1 = Person("Rex")
p1.qwerty(23)

p2 = Person("Buddy")
p2.qwerty(30)

print("=" * 60)

class Vehicle:
    def __init__(self, brand, petname, country): # constructor
        self.country = country
        self.brand = brand
        self.petname = petname

    def make(self, doors):
        return f"Hello {self.brand}! you've {doors} doors"

    def nickname(self):
        return f"Hello {self.petname}! made in {self.country}"

v1 = Vehicle("porsche", "buddy", "Germany")
print(v1.make(2))
print(v1.nickname())

print()

v2 = Vehicle("volkswagen", "cherry", "Britain")
print(v2.make(4))
print(v2.nickname())

## INSTANCE vs CLASS ATTRIBUTES (and "static")

class Circle:
    PI = 3.14159  # class attribute

    def __init__(self, radius):
        self.radius = radius  # instance attribute

    def area(self):
        return Circle.PI * self.radius ** 2

c1 = Circle(3)
c2 = Circle(5)

print(c1.area(), c2.area())
print(c1.radius, c2.radius)
print(c1.PI, Circle.PI)

# ENCAPSULATION: PUBLIC, PROTECTED, PRIVATE (access modifiers)

class Account:
    def __init__(self, holder, balance):
        self.holder = holder  # public instance attribute
        self._balance = balance  # protected instance attribute
        self.__pin = "1234"  # private (name-mangled) instance attribute

    def show(self):
        return f"{self.holder}: {self._balance}"

a = Account("Alice", 500)
print(a.show())
print(a.holder)  # public access - fine
print(a._balance)  # still accessible, python nature
print(a._Account__pin)  # (_Class__Attr) still accessible, python nature

# ENCAPSULATION: METHOD TYPES (instance, class, static, property)

class Employee:
    company = "Acme" # class attribute
    _count = 0 # protected class attribute

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        Employee._count += 1

    def info(self):  # instance method
        return f"{self.name} at {self.company}"

    @classmethod
    def total(cls):  # class method
        return cls._count

    @staticmethod
    def is_valid_salary(amount):  # static method
        return amount > 0

    @property
    def salary(self):  # property: get salary
        return self._salary

    @salary.setter
    def salary(self, value): # setter
        if value < 0:
            raise ValueError("salary cannot be negative")
        self._salary = value

e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 45000)

print(e1.info())  # instance method needs an instance
print(Employee.total())  # class method works on the class itself
print(Employee.is_valid_salary(100)) # static: no self, no cls
print(e1.salary)  # property: no parentheses
e1.salary = 60000  # setter
print(e1.salary)

# INHERITANCE

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def brand_name(self):
        return f"I am {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, doors): # If constructor is not defined, then super() is optional
        super().__init__(brand)  # let Vehicle set self.brand
        self.doors = doors

car = Car("Toyota", 4)
print(car.brand_name(), car.doors)

## MULTIPLE INHERITANCE

class Swimmer:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return "swimming"

class Flyer:
    def fly(self):
        return "flying"

class Duck(Swimmer, Flyer):
    pass

d = Duck("Donald")
print(d.swim(), d.fly())

# POLYMORPHISM

class Cow:
    def speak(self):
        return "Moo"

class Bird:
    def speak(self):
        return "Tweet"

for animal in [Cow(), Bird()]:
    print(animal.speak())

## METHOD OVERRIDING
## Child class redefines a method from the parent with different behavior.

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):  # overrides Shape.area
        return self.side ** 2

print(Shape().area())    # 0
print(Square(5).area())  # 25

## METHOD OVERLOADING (Python doesn't allow that)
## In Java/C++ you can declare multiple methods with the same name but different parameters.

## OPERATOR OVERLOADING (polymorphism via dunder methods)
## Python has about 100+ dunders & Python only recognizes the predefined ones.
"""
    __add__     : x + y
    __getitem__ : x[i]
    __iter__    : for v in x
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # enables  v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):  # enables  v1 == v2
        return self.x == other.x and self.y == other.y

    # Representation, wherever python needs to show the object, then it calls automatically
    def __repr__(self):  # how it shows when printed
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2) # v1.__add__(v2)
print(v1 == Vector(1, 2)) # v1.__eq__(v2)

# ABSTRACTION

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Must implement pay method
class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} by credit card"

# Must implement pay method
class UPI(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} by UPI"

# PaymentMethod()                       # TypeError: can't instantiate abstract class
print(CreditCard().pay(500))
print(UPI().pay(500))