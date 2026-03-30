# Python 速通学习手册（C++ 转 Python）

> 2 小时掌握 Python，代码文件 + 讲解文档配套学习。

---

## 学习路径

| 顺序 | 代码文件                | 配套文档                    | 时间   |
|------|-------------------------|-----------------------------|--------|
| 1    | `01_basics.py`          | `DOC_01_basics.md`          | 20 min |
| 2    | `02_data_structures.py` | `DOC_02_data_structures.md` | 20 min |
| 3    | `03_oop.py`             | `DOC_03_oop.md`             | 20 min |
| 4    | `04_advanced.py`        | `DOC_04_advanced.md`        | 20 min |
| 5    | `05_demo_projects.py`   | `DOC_05_demo_projects.md`   | 40 min |

**使用方法**：左边打开 `.py` 文件运行/修改代码，右边打开对应 `.md` 文档阅读讲解。

---

## C++ → Python 核心差异速查

### 语法

| C++                         | Python                        |
|-----------------------------|-------------------------------|
| `int x = 10;`               | `x = 10`                      |
| `{` `}` 花括号定义块        | **缩进**定义块                |
| `//` 单行注释               | `#` 单行注释                  |
| `/* */` 多行注释            | `"""` 三引号字符串            |
| `cout << x << endl;`        | `print(x)`                    |
| `cin >> x;`                 | `x = input()`                 |
| `x++` / `x--`               | `x += 1` / `x -= 1`（无 `++`）|
| `a ? b : c`                 | `b if a else c`               |

### 数据结构

| C++                         | Python        | 特点                    |
|-----------------------------|---------------|-------------------------|
| `vector<T>`                 | `list`        | 异构，支持切片          |
| `array<T,N>` / `pair`       | `tuple`       | 不可变                  |
| `unordered_map<K,V>`        | `dict`        | 3.7+ 有序               |
| `unordered_set<T>`          | `set`         | 支持集合运算符          |
| `deque<T>`                  | `collections.deque` | 两端 O(1)         |
| `string`                    | `str`         | 不可变，切片强大        |

### 函数

| C++                              | Python                          |
|----------------------------------|---------------------------------|
| `int f(int a, int b=0)`          | `def f(a, b=0):`                |
| 不支持关键字调用                 | `f(b=1, a=2)` 关键字任意顺序   |
| 模板可变参数                     | `def f(*args, **kwargs):`       |
| `auto f = [](int x){ return x; }` | `f = lambda x: x`              |

### 内存管理

| C++                         | Python                          |
|-----------------------------|---------------------------------|
| `new` / `delete` 手动管理   | GC 自动回收，无需手动           |
| RAII（构造/析构）           | `with` 语句 + `__enter__/exit__`|
| `nullptr`                   | `None`                          |
| 栈/堆分配                   | 所有对象在堆上，变量是引用      |
| 拷贝构造                    | `copy.copy()` / `copy.deepcopy()`|

### OOP

| C++                              | Python                        |
|----------------------------------|-------------------------------|
| `class Foo : public Bar`         | `class Foo(Bar):`             |
| `Bar::Bar(args)` 初始化列表      | `super().__init__(args)`      |
| `virtual` 方法                   | 默认全是虚方法                |
| `operator<<`                     | `__str__` / `__repr__`        |
| `operator+`                      | `__add__`                     |
| `static` 成员                    | 类变量 / `@classmethod`       |
| `friend`                         | 无（约定 `_` 前缀）           |

---

## Python 独有特性（C++ 没有的）

```python
# 1. 列表/字典/集合推导式
squares = [x**2 for x in range(10) if x % 2 == 0]

# 2. 多重赋值 & 解包
a, b = b, a          # 交换，无需 temp
first, *rest = lst   # 星号解包

# 3. 链式比较
if 0 < x < 100: ...

# 4. 负索引 & 切片
lst[-1]       # 最后一个元素
lst[::-1]     # 反转

# 5. 生成器：惰性求值，O(1) 内存处理无限序列
def naturals():
    n = 0
    while True:
        yield n
        n += 1

# 6. 装饰器：函数包装的语法糖
@lru_cache(maxsize=128)
def fib(n): ...

# 7. with 语句：自动资源管理
with open("f.txt") as f: ...

# 8. f-string 调试
print(f"{x = }")   # x = 42

# 9. 一切皆对象，函数可以有属性
def f(): pass
f.metadata = "hello"   # 给函数贴属性

# 10. for-else
for x in lst:
    if condition: break
else:
    print("no break occurred")
```

---

## 运行方式

```bash
cd /home/vect/Python/python_crash_course

python3 01_basics.py
python3 02_data_structures.py
python3 03_oop.py
python3 04_advanced.py
python3 05_demo_projects.py
```

学完后推荐方向：
- **数据处理**：`pandas`、`numpy`
- **Web 开发**：`FastAPI`、`Flask`
- **自动化脚本**：`pathlib`、`subprocess`、`requests`
- **机器学习**：`scikit-learn`、`pytorch`
