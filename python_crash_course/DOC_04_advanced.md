# Phase 4：进阶特性精讲

---

## 1. 异常处理

### 完整结构

C++ 只有 `try/catch`，Python 多了 `else` 和 `finally`：

```python
try:
    result = risky_operation()
except SpecificError as e:           # 捕获特定异常
    handle(e)
except (TypeError, ValueError) as e: # 同时捕获多种
    handle(e)
except Exception as e:               # 兜底（慎用）
    log(e)
else:
    # 仅当 try 「没有」异常时执行 —— 把成功路径分离出来
    use(result)
finally:
    # 无论如何都执行，类比 C++ RAII 析构
    cleanup()
```

### 异常层级

```
BaseException
├── SystemExit          ← sys.exit()，别捕获
├── KeyboardInterrupt   ← Ctrl+C，别捕获
└── Exception
    ├── ValueError      ← 值不合法 int("abc")
    ├── TypeError       ← 类型错误 1 + "a"
    ├── IndexError      ← 列表越界
    ├── KeyError        ← 字典键不存在
    ├── FileNotFoundError
    ├── ZeroDivisionError
    └── RuntimeError
```

### 自定义异常

```python
class AppError(Exception): """应用异常基类"""

class ConnectionError(AppError):
    def __init__(self, host, port, reason):
        super().__init__(f"Cannot connect {host}:{port}: {reason}")
        self.host, self.port = host, port

try:
    connect("db", 5432)
except ConnectionError as e:
    print(e.host)   # 访问自定义字段
```

### 异常链

```python
try:
    open("config.json")
except FileNotFoundError as e:
    raise RuntimeError("Config missing") from e  # 保留原始 traceback
```

---

## 2. 文件操作与 with 语句

### with = C++ RAII

```python
# with 语句保证文件一定会关闭，即使发生异常
with open("data.txt", encoding="utf-8") as f:
    data = f.read()

# 同时打开多个文件
with open("in.txt") as fin, open("out.txt", "w") as fout:
    fout.write(fin.read())
```

### 读取方式

```python
f.read()           # 全部内容 → str
f.read(1024)       # 最多 1024 字节
f.readline()       # 一行（含 \n）
f.readlines()      # 所有行 → list

# 最 Pythonic：文件对象本身就是迭代器，逐行无需全部加载到内存
with open("big.log") as f:
    for line in f:
        process(line.rstrip())
```

### pathlib 现代路径操作

```python
from pathlib import Path

p = Path("/home/user") / "config" / "app.json"  # / 拼接路径

p.name      # "app.json"
p.stem      # "app"
p.suffix    # ".json"
p.parent    # /home/user/config

p.exists()  # 是否存在
p.is_file() / p.is_dir()
p.mkdir(parents=True, exist_ok=True)
p.unlink()  # 删除

# 直接读写，省去 open()
text = p.read_text(encoding="utf-8")
p.write_text("hello", encoding="utf-8")

# 递归查找
for py in Path(".").glob("**/*.py"):
    print(py)
```

---

## 3. 生成器（Generator）

### 核心：yield 暂停执行

C++ 没有原生生成器（C++20 协程除外）。`yield` 让函数在此暂停，下次 `next()` 从断点继续：

```python
def countdown(n):
    while n > 0:
        yield n     # 暂停，把 n 返回给调用方
        n -= 1      # 下次 next() 从这里继续

g = countdown(3)    # 不执行任何代码，只创建生成器对象
next(g)  # 3
next(g)  # 2
next(g)  # 1
next(g)  # StopIteration

for n in countdown(5):  # for 循环自动处理 StopIteration
    print(n)
```

### 为什么用生成器：内存效率

```python
# ❌ 列表：10GB 文件全部读入内存
lines = [line for line in open("huge.log")]  # OOM！

# ✅ 生成器：同一时刻内存里只有一行
def read_log(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

for line in read_log("huge.log"):
    if "ERROR" in line:
        print(line)
        break   # 找到即停，剩余内容根本不读取
```

### 生成器表达式 vs 列表推导

```python
# 列表推导 []：立即计算，全部放入内存
big = [x**2 for x in range(1_000_000)]   # ~8MB

# 生成器表达式 ()：惰性计算，几乎 0 内存
gen = (x**2 for x in range(1_000_000))   # ~200 字节

# 原则：只遍历一次 → 生成器；需要索引/多次遍历 → 列表
total = sum(x**2 for x in range(1_000_000))  # 直接传生成器给 sum
```

### yield from

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)  # 委托给递归
        else:
            yield item

list(flatten([1, [2, [3, 4]], 5]))  # [1, 2, 3, 4, 5]
```

---

## 4. 装饰器（Decorator）

### 本质：函数包装函数

```python
@timer
def my_func(): ...

# 完全等价于：
def my_func(): ...
my_func = timer(my_func)   # 用 timer 包装后重新绑定
```

### 标准装饰器模板

```python
import functools

def my_decorator(func):
    @functools.wraps(func)   # 必须加！保留 __name__、__doc__
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper
```

### 带参数的装饰器（三层嵌套）

```python
def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")   # 打印 3 次
```

### 标准库内置装饰器

```python
from functools import lru_cache, cached_property

# memoization 缓存（递归提速神器）
@lru_cache(maxsize=128)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

fib(50)   # 瞬间完成（无缓存的朴素递归要指数时间）

# cached_property：第一次计算后缓存到实例
class Circle:
    def __init__(self, r): self.r = r

    @cached_property
    def area(self):         # 只计算一次，结果存为实例属性
        import math
        return math.pi * self.r ** 2
```

---

## 5. 上下文管理器

实现 `__enter__` / `__exit__` 即可支持 `with` 语句，这是 Python 的 RAII：

```python
class DBConnection:
    def __enter__(self):
        self.conn = connect_db()
        return self.conn          # as 后面的变量

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()         # 无论是否异常都执行
        return False              # False = 不吞掉异常

with DBConnection() as conn:
    conn.execute("SELECT 1")
# 退出 with 块后连接自动关闭
```

### 用 contextlib 简化（无需写类）

```python
from contextlib import contextmanager
import time

@contextmanager
def timer(label=""):
    start = time.perf_counter()
    yield                   # yield 前 = __enter__
    elapsed = time.perf_counter() - start  # yield 后 = __exit__
    print(f"{label}: {elapsed:.4f}s")

with timer("sort"):
    sorted(range(1_000_000, 0, -1))
```

---

## 6. 类型提示（Type Hints）

Python 3.5+ 支持类型注解。**运行时不强制**，但 IDE 和 mypy 可静态检查：

```python
from typing import Optional, Union, List, Dict, Tuple, Callable

def greet(name: str, times: int = 1) -> str:
    return ("Hello, " + name + "! ") * times

# Optional[X] = Union[X, None]
def find(user_id: int) -> Optional[Dict]:
    db = {1: {"name": "Alice"}}
    return db.get(user_id)

# 复杂类型
def process(
    items: List[int],
    transform: Callable[[int], int],   # 函数类型
) -> Dict[str, List[int]]:
    return {"result": [transform(x) for x in items]}

# Python 3.10+ 可以用 | 替代 Union
def f(x: int | str) -> int | None: ...

# Python 3.9+ 内置类型直接用小写
def g(items: list[int]) -> dict[str, int]: ...
```

---

## 7. 练习建议

打开 `04_advanced.py`，尝试：

1. 写一个 `@cache_result(seconds=5)` 装饰器，缓存结果 5 秒后过期
2. 用生成器实现一个无限序列（素数生成器），取前 20 个素数
3. 实现一个 `safe_open` 上下文管理器，文件不存在时返回空字符串而不是抛异常
4. 给 `safe_divide` 加上日志装饰器，记录每次调用的参数和结果
