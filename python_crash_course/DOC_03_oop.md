# Phase 3：面向对象精讲

---

## 1. 类的基本结构

### C++ vs Python 完整对比

```cpp
// C++
class Animal {
public:
    std::string name;
protected:
    int _age;
private:
    int __id;

    Animal(std::string n, int a) : name(n), _age(a) {}
    virtual std::string speak() { return "..."; }
    friend std::ostream& operator<<(std::ostream& os, const Animal& a);
};
```

```python
# Python
class Animal:
    count = 0               # 类变量（类比 C++ static 成员）

    def __init__(self, name: str, age: int):
        self.name = name    # public（约定，无强制）
        self._age = age     # protected（约定：单下划线）
        self.__id = id(self)# private（双下划线 → name mangling）
        Animal.count += 1

    def speak(self) -> str: # virtual 方法（Python 默认都是虚方法）
        return "..."

    def __str__(self) -> str:  # 等价于 operator<<
        return f"Animal({self.name})"
```

### `self` 是什么？

`self` 就是 C++ 的 `this` 指针，但在 Python 中**必须显式写出来**作为第一个参数。调用时 Python 自动传入，无需手动传：

```python
animal = Animal("Rex", 3)
animal.speak()           # Python 自动将 animal 作为 self 传入
# 等价于：Animal.speak(animal)
```

### 访问控制：约定而非强制

| 命名            | 含义         | C++ 等价    | 可否从外部访问    |
|-----------------|--------------|-------------|------------------|
| `name`          | public       | `public`    | 可以              |
| `_name`         | protected    | `protected` | 可以（但约定别用）|
| `__name`        | private      | `private`   | 不建议（name mangling 后变 `_ClassName__name`）|

```python
class Foo:
    def __init__(self):
        self.pub  = 1
        self._pro = 2
        self.__pri = 3

f = Foo()
print(f.pub)          # 1  ✅
print(f._pro)         # 2  ✅（能访问，但约定不该这样做）
print(f.__pri)        # ❌ AttributeError
print(f._Foo__pri)    # 3  ✅（name mangling 后的真实名字）
```

---

## 2. Property —— getter/setter 的优雅实现

C++ 需要手写 `getAge()` / `setAge()`，Python 用 `@property` 装饰器实现透明访问：

```python
class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def celsius(self) -> float:         # getter
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):    # setter
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:      # 只读属性（无 setter）
        return self._celsius * 9/5 + 32


t = Temperature(100)
print(t.celsius)      # 100    ← 调用 getter，语法像访问字段
print(t.fahrenheit)   # 212.0  ← 只读，动态计算
t.celsius = 0         # ← 调用 setter，语法像字段赋值
t.celsius = -300      # ❌ ValueError
```

**好处**：外部代码用 `t.celsius` 而不是 `t.getCelsius()`，以后想加验证逻辑直接加 setter，外部代码无需改动。

---

## 3. 类方法 vs 静态方法 vs 实例方法

```python
class MyClass:
    class_var = 0

    def instance_method(self):      # 普通方法：第一个参数是实例
        return self.class_var

    @classmethod
    def class_method(cls):          # 类方法：第一个参数是类本身
        return cls.class_var        # 类比 C++ static 方法，但能访问类

    @staticmethod
    def static_method():            # 静态方法：不接收 self 或 cls
        return "I'm just a function inside a class"
```

**classmethod 的典型用途**：工厂方法（另一种构造函数）

```python
class Date:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_string(cls, s: str) -> 'Date':  # 工厂方法
        y, m, d = map(int, s.split('-'))
        return cls(y, m, d)    # 调用构造函数

    @classmethod
    def today(cls) -> 'Date':
        import datetime
        t = datetime.date.today()
        return cls(t.year, t.month, t.day)

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"


d1 = Date(2026, 3, 30)
d2 = Date.from_string("2026-03-30")  # 工厂方法
d3 = Date.today()
print(d2)  # 2026-03-30
```

---

## 4. 继承

```python
# 单继承（C++: class Dog : public Animal）
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 调用父类 __init__
        self.breed = breed           # 子类新增字段

    def speak(self):                 # override 父类方法
        return f"{self.name}: Woof!"

# 多继承（C++ 也支持，但 Python 用 MRO 解决菱形问题）
class Flyable:
    def fly(self): return "I can fly!"

class SwimmingDog(Dog, Flyable):    # 多继承
    pass

d = SwimmingDog("Rex", 3, "Lab")
print(d.speak())   # 继承自 Dog
print(d.fly())     # 继承自 Flyable
```

### MRO（方法解析顺序）

Python 用 C3 线性化算法处理多继承，通过 `类.mro()` 查看：

```python
print(SwimmingDog.mro())
# [SwimmingDog, Dog, Animal, Flyable, object]
# 方法查找按此顺序进行
```

### `super()` 的用法

```python
class A:
    def hello(self):
        print("A.hello")

class B(A):
    def hello(self):
        super().hello()   # 调用 MRO 中下一个类的方法
        print("B.hello")

class C(B):
    def hello(self):
        super().hello()   # 调用 B.hello（B 又调用 A.hello）
        print("C.hello")

C().hello()
# A.hello
# B.hello
# C.hello
```

---

## 5. 特殊方法（Dunder Methods）

这是 Python 面向对象最强大的特性之一，通过实现 `__xxx__` 方法让自定义类融入 Python 生态：

| 方法              | 触发场景                    | C++ 等价              |
|-------------------|-----------------------------|-----------------------|
| `__init__`        | `obj = MyClass()`           | 构造函数              |
| `__del__`         | 对象被 GC 回收              | 析构函数              |
| `__str__`         | `str(obj)` / `print(obj)`   | `operator<<`          |
| `__repr__`        | REPL 中显示 / `repr(obj)`   | -                     |
| `__len__`         | `len(obj)`                  | `size()`              |
| `__getitem__`     | `obj[key]`                  | `operator[]`          |
| `__setitem__`     | `obj[key] = val`            | `operator[]` (左值)   |
| `__contains__`    | `x in obj`                  | -                     |
| `__iter__`        | `for x in obj:`             | `begin()/end()`       |
| `__add__`         | `obj + other`               | `operator+`           |
| `__eq__`          | `obj == other`              | `operator==`          |
| `__lt__`          | `obj < other`               | `operator<`           |
| `__call__`        | `obj(args)`                 | `operator()`          |
| `__enter__/exit__`| `with obj:`                 | RAII 构造/析构        |

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, val):  self._data.append(val)
    def pop(self):        return self._data.pop()

    def __len__(self):    return len(self._data)       # len(stack)
    def __bool__(self):   return len(self._data) > 0   # if stack:
    def __contains__(self, val): return val in self._data  # x in stack
    def __iter__(self):   return iter(self._data)      # for x in stack:
    def __str__(self):    return f"Stack{self._data}"

    def __getitem__(self, idx):   # stack[i] 或 stack[1:3]
        return self._data[idx]

s = Stack()
for v in [1, 2, 3, 4]:
    s.push(v)

print(len(s))        # 4
print(bool(s))       # True
print(3 in s)        # True
print(s[1:3])        # [2, 3]
for x in s:
    print(x, end=" ") # 1 2 3 4
```

---

## 6. dataclass —— 消除样板代码

C++ 的简单结构体（struct）在 Python 里写起来要重复很多代码：

```python
# 没有 dataclass：需要手写 __init__、__repr__、__eq__
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

用 `@dataclass` 装饰器，这些全部自动生成：

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Point:
    x: float
    y: float
    label: str = ""            # 带默认值的字段

# 自动生成：__init__, __repr__, __eq__
p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0)
print(p1)           # Point(x=1.0, y=2.0, label='')
print(p1 == p2)     # True

# 不可变 dataclass（类比 C++ const struct）
@dataclass(frozen=True)
class ImmutablePoint:
    x: float
    y: float

# 带复杂默认值（不能直接写 []，要用 field(default_factory=...)）
@dataclass
class Student:
    name: str
    grades: List[float] = field(default_factory=list)  # 每个实例独立的 list
    _id: int = field(default=0, repr=False)            # 不出现在 repr 里
```

---

## 7. 练习建议

打开 `03_oop.py`，尝试：

1. 给 `Vector2D` 增加 `__sub__`（减法）和 `__neg__`（取反）
2. 实现一个 `Rectangle` dataclass，包含 `area` 和 `perimeter` 两个 property
3. 用继承 + `__str__` 实现一个 `ColoredPoint(Point)` 带颜色属性
4. 实现 `__iter__` 让 `Vector2D` 可以用 `for coord in v:` 遍历
