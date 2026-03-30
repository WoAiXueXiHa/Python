# ============================================================
# Phase 2: 核心数据结构 + 函数
# ============================================================

# ── 1. List（动态数组，类比 C++ vector<T>）────────────────
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.append(7)          # push_back
nums.pop()              # pop_back
nums.insert(0, 0)       # 在index 0 插入
nums.remove(1)          # 删除第一个值为1的元素
print(nums)

# 切片操作（C++没有这么方便的语法）
print(nums[1:4])        # index 1,2,3
print(nums[::2])        # 每隔一个取一个

# 排序
nums.sort()             # 原地排序
nums.sort(reverse=True) # 降序
sorted_nums = sorted(nums)  # 返回新列表，不修改原列表

# 列表推导式（C++没有，非常强大！）
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]
matrix  = [[i*j for j in range(3)] for i in range(3)]
print("squares:", squares)
print("evens:",   evens)
print("matrix:",  matrix)

# ── 2. Tuple（不可变列表，类比 const vector + pair）───────
point = (3, 4)
x, y = point            # 解包！
print(f"x={x}, y={y}")

# 函数返回多值（实际返回 tuple）
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max(nums)
print(f"min={lo}, max={hi}")

# ── 3. Dict（哈希表，类比 C++ unordered_map）─────────────
person = {
    "name": "Alice",
    "age":  25,
    "langs": ["C++", "Python"]
}
print(person["name"])
person["city"] = "Beijing"      # 添加键
person.get("email", "N/A")       # 安全访问，默认值 N/A

# 遍历
for key, value in person.items():
    print(f"  {key}: {value}")

# 字典推导式
word_len = {w: len(w) for w in ["hello", "world", "python"]}
print(word_len)

# ── 4. Set（集合，类比 C++ unordered_set）─────────────────
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
print(s1 & s2)          # 交集 {3, 4, 5}
print(s1 | s2)          # 并集
print(s1 - s2)          # 差集 {1, 2}

# ── 5. 函数 ───────────────────────────────────────────────
# 基本函数（C++: int add(int a, int b) { return a + b; }）
def add(a, b):
    return a + b

# 默认参数
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Bob"))
print(greet("Bob", "Hi"))

# 关键字参数（调用时可乱序）
def create_user(name, age, city="Unknown"):
    return {"name": name, "age": age, "city": city}

user = create_user(age=30, name="Charlie", city="Shanghai")
print(user)

# *args 可变参数（类比 variadic templates）
def total(*args):
    return sum(args)

print(total(1, 2, 3, 4, 5))   # 15

# **kwargs 关键字可变参数
def print_info(**kwargs):
    for k, v in kwargs.items():
        print(f"  {k} = {v}")

print_info(name="Alice", age=25, lang="Python")

# Lambda（匿名函数，类比 C++ lambda）
# C++: auto square = [](int x) { return x * x; };
square = lambda x: x ** 2
print(list(map(square, range(5))))    # map 应用函数到每个元素
print(list(filter(lambda x: x > 2, range(5))))  # filter 过滤

# ── 6. 内置高阶函数 ───────────────────────────────────────
from functools import reduce

nums = [1, 2, 3, 4, 5]
print(sum(nums))                              # 15
print(max(nums), min(nums))                   # 5 1
print(reduce(lambda a, b: a * b, nums))       # 120（阶乘）

# sorted with key
words = ["banana", "apple", "cherry", "date"]
print(sorted(words, key=len))                 # 按长度排序
print(sorted(words, key=lambda w: w[-1]))     # 按最后一个字母排序
