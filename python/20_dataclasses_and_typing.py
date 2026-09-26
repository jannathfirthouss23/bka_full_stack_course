# Dataclasses auto-generate __init__, __repr__, and __eq__ for us.

# WITHOUT DATACLASS (the old way)

class PersonOld:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"PersonOld(name={self.name!r}, age={self.age})"

p = PersonOld("Alice", 30)
print(p)

# WITH @DATACLASS

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person("Alice", 30)
print(p)                                # repr is free
print(p == Person("Alice", 30))         # equality is free

# DEFAULT VALUES

@dataclass
class Product:
    name: str
    price: float = 0.0
    stock: int = 0

    def stock_value(self):
        return self.price * self.stock

print(Product("Pen"))
print(Product("Book", 12.99, 50))
print(Product("Book", 12.99, 50).stock_value())

# MUTABLE DEFAULTS (use field(default_factory=...))

from dataclasses import field

@dataclass
class Team:
    name: str
    members: list = field(default_factory=list)

t = Team("Engineering")
t.members.append("Alice")
print(t)

# FROZEN (immutable dataclass)

@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(3, 4)
print(p)
# p.x = 10                              # raises FrozenInstanceError

# BASIC TYPE HINTS

def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

print(greet("Alice"))
print(add(3, 4))

# COMMON TYPE HINTS

def process(items: list[int]) -> dict[str, int]:
    return {"sum": sum(items), "count": len(items)}

print(process([1, 2, 3]))

# OPTIONAL (value or None)

def first_or_none(items: list[int]) -> int | None:
    return items[0] if items else None

print(first_or_none([10, 20]))
print(first_or_none([]))

# UNION TYPES (one of several types)

def stringify(value: int | float | str) -> str:
    return str(value)

print(stringify(42))
print(stringify(3.14))
print(stringify("hi"))

# HINTS ARE NOT ENFORCED

def strict(n: int) -> int:
    return n * 2

print(strict(5))
print(strict("hi"))                     # no error - hint ignored at runtime, because python treats like suggestions.