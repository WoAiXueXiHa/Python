# Phase 2：核心数据结构 + 函数精讲

---

## 1. List —— Python 的瑞士军刀

### 对比 C++ `std::vector<T>`

| 操作          | C++                        | Python               |
|---------------|----------------------------|----------------------|
| 创建          | `vector<int> v = {1,2,3};` | `v = [1, 2, 3]`      |
| 末尾添加      | `v.push_back(4)`           | `v.append(4)`        |
| 末尾删除      | `v.pop_back()`             | `v.pop()`            |
| 指定位置插入  | `v.insert(v.begin(), 0)`   | `v.insert(0, val)`   |
| 按值删除      | `v.erase(find(...))`       | `v.remove(val)`      |
| 长度          | `v.size()`                 | `len(v)`             |
| 访问元素      | `v[i]`                     | `v[i]`（支持负索引） |
| 遍历          | range-for                  | `for x in v:`        |
| 包含判断      | `find != v.end()`          | `val in v`           |

关键区别：
- Python list 是**异构容器**，可以混放任意类型：`[1, "hello", 3.14, True]`
- Python list 底层是**动态数组**（和 vector 一样），随机访问 O(1)，中间插入 O(n)
- **无需指定类型**，一个 list 可以存不同类型的对象

### 切片操作 `[start:end:step]`

切片是 Python 序列操作的核心，返回**新列表**（浅拷贝），不修改原列表：

```python
v = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

v[2:5]    # [2, 3, 4]        取 index 2,3,4（左闭右开）
v[:3]     # [0, 1, 2]        从头到 index 2
v[7:]     # [7, 8, 9]        从 index 7 到末尾
v[::2]    # [0, 2, 4, 6, 8]  每隔一个取一个
v[::-1]   # [9,8,...,0]       反转！
v[1:8:2]  # [1, 3, 5, 7]     从1开始，步长2，到8前结束

# 切片赋值（C++ 没有等价操作）
v[2:5] = [20, 30, 40]  # 替换指定范围
v[::2] = [0]*5         # 替换偶数索引位置
```

### 列表推导式（List Comprehension）

这是 Python 最具代表性的特性之一，用一行代替 C++ 的 transform + filter：

```python
# C++ 风格（繁琐）:
# vector<int> squares;
# for (int x = 0; x < 10; x++) squares.push_back(x*x);

# Python（简洁）:
squares = [x**2 for x in range(10)]

# 带过滤条件（相当于 C++ filter + transform）
evens = [x for x in range(20) if x % 2 == 0]

# 嵌套推导（生成矩阵）
matrix = [[i*j for j in range(4)] for i in range(4)]

# 字符串处理
words = ["hello", "WORLD", "Python"]
lower = [w.lower() for w in words]      # ['hello', 'world', 'python']
lengths = [len(w) for w in words]       # [5, 5, 6]

# 扁平化二维列表（flatten）
nested = [[1,2,3],[4,5,6],[7,8,9]]
flat = [x for row in nested for x in row]  # [1,2,3,4,5,6,7,8,9]
```

---

## 2. Tuple —— 不可变序列

Tuple 与 list 的唯一区别：**创建后不能修改**。

```python
point = (3, 4)      # 用圆括号（也可以不加括号：point = 3, 4）
point[0] = 10       # ❌ TypeError: tuple 不支持赋值
```

**什么时候用 tuple？**
- 函数返回多个值：`return x, y, z`（本质就是返回 tuple）
- 字典的 key（list 不能做 key，因为不可哈希）
- 表示固定结构的数据：坐标、RGB 颜色、数据库记录
- 性能略优于 list（不可变对象有优化空间）

### 解包（Unpacking）

```python
# 基础解包
x, y = (3, 4)
name, age, city = ("Alice", 25, "Beijing")

# 函数返回多值
def divmod_custom(a, b):
    return a // b, a % b   # 返回 tuple

quotient, remainder = divmod_custom(17, 5)
# quotient=3, remainder=2

# 星号解包
first, *rest = (1, 2, 3, 4, 5)
# first=1, rest=[2,3,4,5]  注意 rest 是 list！

# 在 for 循环中自动解包
points = [(1,2), (3,4), (5,6)]
for x, y in points:
    print(f"({x}, {y})")
```

---

## 3. Dict —— 哈希表

### 对比 C++ `std::unordered_map<K,V>`

| 操作          | C++                            | Python                     |
|---------------|--------------------------------|----------------------------|
| 创建          | `unordered_map<string,int> m;` | `m = {"a": 1, "b": 2}`    |
| 插入/更新     | `m["key"] = val;`              | `m["key"] = val`           |
| 访问          | `m.at("key")`（越界抛异常）    | `m["key"]`（越界抛异常）   |
| 安全访问      | `m.count(k) ? m[k] : default`  | `m.get(k, default)`        |
| 删除          | `m.erase("key")`               | `del m["key"]`             |
| 存在判断      | `m.count("key") > 0`           | `"key" in m`               |
| 遍历键        | `for (auto& [k,v] : m)`        | `for k in m:` 或 `m.keys()`|
| 遍历键值      | 同上                           | `for k, v in m.items():`   |

### dict 的重要特性（Python 3.7+）

**有序**：Python 3.7 起 dict 保证**插入顺序**，C++ 的 unordered_map 不保证顺序。

```python
# 常用模式
d = {"x": 1, "y": 2}

# 合并两个 dict（Python 3.9+）
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2          # {"a": 1, "b": 2}

# setdefault：键不存在时设置默认值
d.setdefault("z", 0)      # 若 "z" 不存在则插入 0

# 统计词频的经典写法
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = {}
for w in words:
    count[w] = count.get(w, 0) + 1
# 更 Pythonic：用 collections.Counter
from collections import Counter
count = Counter(words)   # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
```

### 字典推导式

```python
# 反转键值
d = {"a": 1, "b": 2, "c": 3}
reversed_d = {v: k for k, v in d.items()}  # {1: 'a', 2: 'b', 3: 'c'}

# 过滤
big = {k: v for k, v in d.items() if v > 1}  # {'b': 2, 'c': 3}

# 从两个列表构建
keys   = ["name", "age", "city"]
values = ["Alice", 25, "Beijing"]
result = dict(zip(keys, values))
# 或: {k: v for k, v in zip(keys, values)}
```

---

## 4. Set —— 集合

对比 C++ `std::unordered_set<T>`，Python set 额外提供数学集合运算符：

```python
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

s1 & s2   # 交集  {3, 4, 5}   — C++: set_intersection
s1 | s2   # 并集  {1,2,3,4,5,6,7}
s1 - s2   # 差集  {1, 2}      — 在 s1 但不在 s2
s1 ^ s2   # 对称差 {1,2,6,7}  — 只在其中一个

s1 <= s2   # s1 是否为 s2 的子集
s1 >= s2   # s1 是否为 s2 的超集

# 最常用场景：去重
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
unique = list(set(nums))   # 去重（顺序不保证）

# 快速成员判断 O(1)（比 list 的 O(n) 快得多）
vocabulary = {"apple", "banana", "cherry"}  # 大词汇表用 set
if "apple" in vocabulary:
    print("found")
```

---

## 5. 函数

### 默认参数与关键字参数

```python
def connect(host, port=5432, ssl=True, timeout=30):
    print(f"Connecting to {host}:{port} ssl={ssl}")

# 调用方式（C++ 只支持前两种）
connect("localhost")                      # 只传必需参数
connect("localhost", 3306)                # 按顺序
connect("localhost", ssl=False)           # 跳过 port，指定 ssl
connect(timeout=60, host="db.server")    # 完全乱序！
```

⚠️ **坑：默认参数使用可变对象**
```python
# ❌ 错误写法——所有调用共享同一个列表！
def append_to(val, lst=[]):
    lst.append(val)
    return lst

append_to(1)   # [1]
append_to(2)   # [1, 2]  ← 不是 [2]！

# ✅ 正确写法
def append_to(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    return lst
```

### `*args` 和 `**kwargs`

```python
# *args：收集多余位置参数为 tuple
def log(*args):
    for msg in args:
        print(f"[LOG] {msg}")

log("start", "processing", "done")

# **kwargs：收集多余关键字参数为 dict
def create_tag(tag, **attrs):
    attr_str = " ".join(f'{k}="{v}"' for k, v in attrs.items())
    return f"<{tag} {attr_str}>"

print(create_tag("a", href="/home", class_="btn", id="nav"))
# <a href="/home" class_="btn" id="nav">

# 展开传参（反向操作，类比 C++ 参数包展开）
def add(a, b, c):
    return a + b + c

args_list = [1, 2, 3]
print(add(*args_list))      # 等价于 add(1, 2, 3)

kw = {"a": 1, "b": 2, "c": 3}
print(add(**kw))             # 等价于 add(a=1, b=2, c=3)
```

### Lambda 与高阶函数

```python
# lambda 语法：lambda 参数: 表达式（只能是单个表达式）
# C++: auto f = [](int x) { return x * x; };
square = lambda x: x ** 2
add    = lambda x, y: x + y

# map：对每个元素应用函数（惰性，返回迭代器）
result = list(map(lambda x: x**2, [1,2,3,4,5]))
# 更 Pythonic：用列表推导代替
result = [x**2 for x in [1,2,3,4,5]]

# filter：过滤满足条件的元素
evens = list(filter(lambda x: x%2==0, range(10)))
# 更 Pythonic：
evens = [x for x in range(10) if x%2==0]

# sorted with key——非常常用！
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

# 按成绩升序
sorted_by_score = sorted(students, key=lambda s: s[1])
# 