# ============================================================
# Phase 3: 面向对象（对比C++理解）
# ============================================================

# ── 1. 基础类 ─────────────────────────────────────────────
# C++:
# class Animal {
# public:
#     std::string name;
#     int age;
#     Animal(std::string n, int a) : name(n), age(a) {}
#     virtual std::string speak() { return "..."; }
# };

class Animal:
    # 类变量（所有实例共享，类比 C++ static 成员）
    count = 0

    # __init__ 是构造函数，self 类比 C++ 的 this 指针
    def __init__(self, name: str, age: int):
        self.name = name        # 实例变量（public）
        self._age  = age        # 约定 _前缀 = protected
        self.__id  = id(self)   # 约定 __前缀 = private（name mangling）
        Animal.count += 1

    # 普通方法
    def speak(self) -> str:
        return "..."

    # __str__ 类比 C++ 的 operator<<
    def __str__(self) -> str:
        return f"Animal({self.name}, {self._age})"

    # __repr__：开发者可读的表示（在 REPL 中显示）
    def __repr__(self) -> str:
        return f"Animal(name={self.name!r}, age={self._age!r})"

    # Property：getter/setter 语法糖（类比 C++ getAge/setAge）
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    # 类方法（类比 C++ static method，接收类本身而非实例）
    @classmethod
    def get_count(cls):
        return cls.count

    # 静态方法（纯工具函数，不接收 self 或 cls）
    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and len(name) > 0


# ── 2. 继承 ───────────────────────────────────────────────
# C++: class Dog : public Animal { ... };

class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)    # 调用父类构造函数
        self.breed = breed

    # 方法重写（override）
    def speak(self) -> str:
        return f"{self.name} says: Woof!"

    def __str__(self) -> str:
        return f"Dog({self.name}, breed={self.breed})"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says: Meow!"


# ── 3. 多态 ───────────────────────────────────────────────
# Python 是鸭子类型：不需要声明接口，只需对象有对应方法
animals = [
    Dog("Rex",      3, "Husky"),
    Cat("Whiskers", 5),
    Dog("Buddy",    2, "Labrador"),
]

for animal in animals:
    print(animal.speak())   # 多态调用

print(f"Total animals created: {Animal.get_count()}")

# ── 4. 特殊方法（dunder methods）─────────────────────────
# 类比 C++ 运算符重载

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):           # v1 + v2
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):          # v * 3
        return Vector2D(self.x * scalar, self.y * scalar)

    def __len__(self):                  # len(v)
        return 2

    def __getitem__(self, idx):         # v[0], v[1]
        return (self.x, self.y)[idx]

    def __eq__(self, other):            # v1 == v2
        return self.x == other.x and self.y == other.y

    def __abs__(self):                  # abs(v) -> magnitude
        return (self.x**2 + self.y**2) ** 0.5

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"


v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
print(v1 + v2)          # Vector2D(4, 6)
print(v1 * 3)           # Vector2D(3, 6)
print(abs(v2))          # 5.0
print(v2[0], v2[1])     # 3 4

# ── 5. dataclass（Python 3.7+，减少样板代码）─────────────
# 类比 C++ struct with auto-generated ==, repr
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float
    label: str = ""     # 带默认值的字段

    def distance_to(self, other: 'Point') -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5


p1 = Point(0.0, 0.0, "origin")
p2 = Point(3.0, 4.0)
print(p1)                        # Point(x=0.0, y=0.0, label='origin')
print(p1.distance_to(p2))        # 5.0
print(p1 == Point(0.0, 0.0, "origin"))  # True（自动生成 __eq__）
