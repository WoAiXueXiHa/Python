# Phase 1：Python 基础语法精讲

> 目标读者：有 C++ 基础，想快速理解 Python 思维模型

---

## 1. 变量与类型系统

### C++ vs Python 核心差异

C++ 是**静态类型**语言：变量声明时绑定类型，编译期检查。
```cpp
int x = 10;          // x 永远是 int
double pi = 3.14;
std::string s = "hello";
```

Python 是**动态类型**语言：变量是标签（引用），类型附着在**对象**上，不在变量上。
```python
x = 10       # x 贴在整数对象 10 上
x = "hello"  # x 现在贴在字符串对象上，完全合法！
x = [1,2,3]  # 再换，也没问题
```

> 类比：C++ 变量是贴了类型标签的**盒子**；Python 变量是**便利贴**，可以随时贴到任何东西上。

### 内置基础类型对照表

| Python      | C++ 等价          | 示例                  |
|-------------|-------------------|-----------------------|
| `int`       | `long long`       | `x = 42`              |
| `float`     | `double`          | `pi = 3.14`           |
| `bool`      | `bool`            | `flag = True`         |
| `str`       | `std::string`     | `s = "hello"`         |
| `None`      | `nullptr` / null  | `val = None`          |
| `complex`   | 无原生支持        | `c = 3 + 4j`          |

⚠️ 注意：Python 的 `int` 没有溢出！它是任意精度整数。
```python
print(2 ** 100)  # 正常输出，C++ 会溢出
```

### 类型检查
```python
type(x)          # 返回类型对象 <class 'int'>
isinstance(x, int)   # 推荐：检查是否为某类型（支持继承）
isinstance(x, (int, float))  # 检查是否为多个类型之一
```

---

## 2. 多重赋值与解包

C++ 交换变量需要临时变量：
```cpp
int tmp = a;
a = b;
b = tmp;
```

Python 利用**元组解包**一行搞定：
```python
a, b = b, a  # 右边先构成 tuple (b, a)，再解包赋值
```

这个特性贯穿 Python 始终，非常常用：
```python
# 函数返回多值
def get_range(lst):
    return min(lst), max(lst)   # 实际返回 tuple

lo, hi = get_range([3,1,4,1,5])

# 星号解包（类比 C++ 结构化绑定的扩展版）
first, *rest = [1, 2, 3, 4, 5]
# first=1, rest=[2,3,4,5]

first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5
```

---

## 3. 字符串：Python 最强内置类型之一

### 索引与切片

Python 字符串支持**负索引**（从末尾倒数）：
```
  H  e  l  l  o  ,     P  y  t  h  o  n  !
  0  1  2  3  4  5  6  7  8  9 10 11 12 13
-14-13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
```

切片语法 `s[start:end:step]`，遵循**左闭右开**原则（和 C++ 迭代器区间一致）：
```python
s = "Hello, Python!"
s[0:5]    # "Hello"     → [0, 5)
s[7:]     # "Python!"   → 省略 end 表示到末尾
s[:5]     # "Hello"     → 省略 start 表示从头
s[::2]    # "HloPto"    → 每隔一个字符取一个
s[::-1]   # "!nohtyP ,olleH" → 步长为 -1 = 反转
```

### f-string 格式化（推荐写法）

f-string 是 Python 3.6+ 的字符串格式化方案，比 C 的 printf / C++ 的 std::format 更直观：
```python
name = "Alice"
age  = 25
pi   = 3.14159

print(f"Name: {name}, Age: {age}")      # 直接嵌入变量
print(f"Pi = {pi:.2f}")                # 格式说明符：保留2位小数
print(f"{1000000:,}")                  # 千位分隔符：1,000,000
print(f"{42:08b}")                     # 二进制，补零到8位：00101010
print(f"{name!r}")                     # repr() 输出：'Alice'（带引号）
print(f"{2 + 3 = }")                   # 调试神器（Python 3.8+）：2 + 3 = 5
```

### 常用字符串方法速查
```python
"  hello  ".strip()          # "hello"       去除首尾空白
"hello".upper()              # "HELLO"
"HELLO".lower()              # "hello"
"hello world".title()        # "Hello World"
"hello".replace("l", "r")   # "herro"
"a,b,c".split(",")          # ["a","b","c"]  分割
",".join(["a","b","c"])     # "a,b,c"        拼接
"hello".startswith("he")    # True
"hello".find("ll")           # 2             找不到返回 -1
"ha" * 3                     # "hahaha"      重复
```

---

## 4. 控制流

### 最重要的规则：**用缩进代替花括号**

```python
# C++                    # Python
# if (x > 0) {           if x > 0:
#     do_a();                do_a()
#     do_b();                do_b()
# }                      # 缩进结束 = 块结束
```

标准缩进是 **4 个空格**（不要用 Tab，混用会报错）。

### Python 独有的链式比较
```python
# C++: if (0 < x && x < 100)
if 0 < x < 100:      # Python 直接这样写！
    ...

if 1 <= n <= 10:     # 同理
    ...
```

### 三元表达式（条件表达式）
```python
# C++: int abs_x = (x >= 0) ? x : -x;
abs_x = x if x >= 0 else -x   # Python 语序：值 if 条件 else 备选值
```

### 真值判断：Python 的隐式 bool

Python 中以下值都被视为 `False`：
- `None`
- `0`、`0.0`、`0j`
- 空序列：`""`、`[]`、`()`、`{}`
- 空集合：`set()`

其余一律为 `True`。这让代码更简洁：
```python
# C++: if (lst.size() > 0)
if lst:              # Python：非空列表即为 True
    ...

# C++: if (ptr != nullptr)
if obj:              # Python：非 None 即为 True
    ...
```

---

## 5. 循环

### for 循环的本质是**迭代**

C++ 的 for 循环本质是计数器控制。Python 的 for 是**迭代协议**——任何实现了 `__iter__` 的对象都能被遍历：

```python
# 遍历范围
for i in range(5):       # 0,1,2,3,4
for i in range(2, 8):    # 2,3,4,5,6,7
for i in range(0,10,2):  # 0,2,4,6,8（步长2）
for i in range(9,-1,-1): # 9,8,...,0（倒序）

# 遍历序列（比 C++ 范围for更通用）
for ch in "hello":       # 遍历字符
for item in [1,2,3]:     # 遍历列表
for k, v in d.items():   # 遍历字典键值对

# 同时获取索引和值（替代 C++ 的 for(int i=0; i<n; i++)）
for i, val in enumerate(["a","b","c"]):
    print(i, val)        # 0 a, 1 b, 2 c

# 同时遍历多个序列
for a, b in zip([1,2,3], ["x","y","z"]):
    print(a, b)          # 1 x, 2 y, 3 z
```

### for-else：Python 独有

```python
# 在列表中搜索目标值
target = 7
for x in [1, 3, 5, 9]:
    if x == target:
        print("Found!")
        break
else:
    # 仅当循环未被 break 中断时执行
    print("Not found")   # ← 会执行这个
```

> 用途：替代 C++ 中搜索后检查「是否找到」的 bool flag 模式。

---

## 6. 练习建议

打开 `01_basics.py`，尝试以下修改：

1. 把 FizzBuzz 改成判断 3/7 倍数
2. 用切片 `s[::-1]` 判断一个字符串是否是回文
3. 用 `enumerate` + `zip` 重写一个双指针遍历
4. 用链式比较写一个温度档位判断（冷/凉/暖/热）
