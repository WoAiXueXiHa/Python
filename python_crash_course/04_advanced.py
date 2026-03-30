# ============================================================
# Phase 4: 文件 / 异常 / 模块 / 迭代器 / 装饰器
# ============================================================

import os
import json
from pathlib import Path

# ── 1. 异常处理 ───────────────────────────────────────────
# C++: try { ... } catch (std::exception& e) { ... }

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except TypeError as e:
        print(f"Type error: {e}")
        return None
    else:
        # 没有异常时执行（C++没有这个）
        print(f"{a} / {b} = {result}")
        return result
    finally:
        # 无论如何都执行（类比 C++ RAII 析构 / finally）
        print("Division attempted.")

safe_divide(10, 2)
safe_divide(10, 0)

# 自定义异常（类比 C++ 继承 std::exception）
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        super().__init__(f"Need {amount}, but balance is {balance}")
        self.amount  = amount
        self.balance = balance

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount

try:
    withdraw(100, 200)
except InsufficientFundsError as e:
    print(f"Caught: {e}")


# ── 2. 文件操作 ───────────────────────────────────────────
# with 语句 = C++ RAII：自动关闭文件（等价于 unique_ptr 析构）
filepath = "/tmp/test_python.txt"

# 写文件
with open(filepath, "w", encoding="utf-8") as f:
    f.write("Hello, Python!\n")
    f.write("Line 2\n")
    f.writelines([f"Line {i}\n" for i in range(3, 6)])

# 读文件
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()          # 全部读入
    # 或者逐行读：for line in f: ...
print(content)

# pathlib（现代写法，比 os.path 更 Pythonic）
p = Path("/tmp")
print(list(p.glob("*.txt")))    # 列出所有 txt 文件
new_file = p / "data.json"      # / 运算符拼接路径！

# JSON
data = {"name": "Alice", "scores": [95, 87, 92]}
new_file.write_text(json.dumps(data, indent=2), encoding="utf-8")
loaded = json.loads(new_file.read_text(encoding="utf-8"))
print(loaded)


# ── 3. 生成器（Generator）────────────────────────────────
# C++ 没有原生等价物（类似协程）
# 用 yield 替代 return，每次调用返回一个值，节省内存

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a             # 暂停并返回值
        a, b = b, a + b

print(list(fibonacci(10)))  # [0,1,1,2,3,5,8,13,21,34]

# 生成器表达式（类比列表推导，但惰性求值）
# 列表推导：立即计算，全部存入内存
big_list = [x**2 for x in range(1_000_000)]  # 占用大量内存
# 生成器：惰性求值，按需计算
big_gen  = (x**2 for x in range(1_000_000))  # 几乎不占内存
print(next(big_gen))    # 0
print(next(big_gen))    # 1


# ── 4. 装饰器（Decorator）────────────────────────────────
# 类比 C++ AOP（面向切面）或 wrapper 模式
# 本质：接收函数，返回增强后的函数

import time
import functools

def timer(func):
    @functools.wraps(func)   # 保留原函数的 __name__ 等元数据
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

def retry(times=3):
    """带参数的装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt+1} failed: {e}")
            return None
        return wrapper
    return decorator

@timer
def slow_sum(n):
    return sum(range(n))

@retry(times=3)
def flaky_function():
    # 演示重试逻辑（固定失败2次，第3次成功）
    flaky_function._calls = getattr(flaky_function, '_calls', 0) + 1
    if flaky_function._calls < 3:
        raise RuntimeError("Simulated failure")
    return "success!"

print(slow_sum(500_000))
print(flaky_function())


# ── 5. 上下文管理器 ───────────────────────────────────────
# 实现 __enter__ / __exit__ 即可用 with 语句
# 类比 C++ RAII

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.4f}s")

with Timer() as t:
    total = sum(range(500_000))
print(f"Sum = {total}")


# ── 6. 类型提示（Type Hints）──────────────────────────────
# Python 3.5+，不强制执行但提高可读性
from typing import List, Dict, Optional, Union, Tuple

def process(items: List[int], multiplier: float = 1.0) -> List[float]:
    return [x * multiplier for x in items]

def find_user(user_id: int) -> Optional[Dict]:
    db = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    return db.get(user_id)  # 可能返回 None

print(process([1, 2, 3], 2.5))
print(find_user(1))
print(find_user(99))    # None
