# ============================================================
# Phase 1: Python 基础语法 (对比C++理解)
# ============================================================

# ── 1. 变量与类型 ──────────────────────────────────────────
# C++: int x = 10; double pi = 3.14; std::string s = "hello";
# Python: 无需声明类型，动态绑定

x = 10
pi = 3.14
name = "Alice"
flag = True
nothing = None          # 等价于 C++ 的 nullptr / null

# 类型检查
print(type(x))          # <class 'int'>
print(type(pi))         # <class 'float'>
print(type(name))       # <class 'str'>

# ── 2. 多重赋值 (C++ 没有这个语法糖) ──────────────────────
a, b, c = 1, 2, 3
a, b = b, a             # 交换变量，无需 temp！

# ── 3. 字符串操作 ─────────────────────────────────────────
# C++: std::string 操作繁琐
s = "Hello, Python!"
print(s[0])             # 'H'         — 索引
print(s[-1])            # '!'         — 负索引（从末尾）
print(s[0:5])           # 'Hello'     — 切片 [start:end)
print(s[::-1])          # 反转字符串！

# f-string 格式化 (类似 C++20 的 std::format)
age = 25
print(f"My name is {name}, age {age}")
print(f"Pi = {pi:.2f}")              # 保留2位小数

# 字符串方法
print("  hello  ".strip())          # "hello"
print("hello".upper())              # "HELLO"
print("a,b,c".split(","))          # ['a', 'b', 'c']
print(",".join(["a", "b", "c"]))   # "a,b,c"

# ── 4. 控制流 ─────────────────────────────────────────────
# C++: if (x > 0) { ... } else { ... }
# Python: 用缩进代替花括号！

if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

# Python 独有：链式比较
if 0 < x < 100:
    print("x is between 0 and 100")

# ── 5. 循环 ───────────────────────────────────────────────
# C++: for (int i = 0; i < 5; i++)
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i, end=" ")   # 0 2 4 6 8
print()

# for-else（C++没有）：循环正常结束时执行 else
for i in range(3):
    if i == 5:
        break
else:
    print("Loop completed without break")

# while 循环
count = 0
while count < 3:
    print(f"count = {count}")
    count += 1
    # 注意：Python 没有 count++ 语法！只有 += 1

# ── 6. 练习题 ─────────────────────────────────────────────
print("\n=== 练习：FizzBuzz ===")
for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()
