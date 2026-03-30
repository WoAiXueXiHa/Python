# Phase 5：综合 Demo 精讲

> 本文件对应 `05_demo_projects.py`，逐个拆解 4 个综合项目的设计思路。

---

## Demo 1：学生成绩管理系统

### 设计要点

**数据建模用 `@dataclass`**

`Student` 用 dataclass 而不是普通类，省去 `__init__` / `__repr__` / `__eq__` 的样板代码。`scores` 字段用 `field(default_factory=list)` 而不是 `scores=[]`，避免所有实例共享同一个列表（这是 Python 新手最常踩的坑）。

```python
@dataclass
class Student:
    name:   str
    scores: List[float] = field(default_factory=list)  # ✅ 每个实例独立
    # scores: List[float] = []  ← ❌ 所有实例共享！
```

**用 `@property` 做计算属性**

`average` 和 `grade` 不存储，每次访问时动态计算。外部代码用 `s.average` 而非 `s.average()`，接口更自然：

```python
@property
def average(self) -> Optional[float]:
    return statistics.mean(self.scores) if self.scores else None

@property
def grade(self) -> str:
    avg = self.average
    if avg is None: return "N/A"
    if avg >= 90:   return "A"
    ...
```

**排序用 `key` 函数**

```python
# sorted() 的 key 参数接受一个函数，返回用于比较的值
def top_students(self, n=3):
    return sorted(
        [s for s in self.students if s.average is not None],
        key=lambda s: s.average,   # 按 average 属性排序
        reverse=True               # 降序
    )[:n]                          # 切片取前 n 个
```

**`statistics` 标准库**

Python 自带统计模块，无需 numpy 即可做基础统计：
```python
import statistics
statistics.mean([1,2,3,4,5])    # 3.0
statistics.stdev([1,2,3,4,5])   # 标准差 1.58
statistics.median([1,2,3,4,5])  # 中位数 3
```

---

## Demo 2：词频分析器

### 设计要点

**正则表达式提取单词**

```python
import re
words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
# \b     = 单词边界（不匹配标点）
# [a-zA-Z]+ = 一个或多个字母
# text.lower() = 先转小写，统计不区分大小写
```

**`collections.Counter` —— 词频统计神器**

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "apple"]
c = Counter(words)
print(c)                    # Counter({'apple': 3, 'banana': 1, 'cherry': 1})
print(c.most_common(2))     # [('apple', 3), ('banana', 1)]
print(c["apple"])           # 3
print(c["missing"])         # 0（不存在的键返回 0，不报 KeyError）

# Counter 支持加减运算
c1 = Counter("hello")
c2 = Counter("world")
print(c1 + c2)  # 合并计数
print(c1 - c2)  # 差集计数
```

**集合过滤停用词**

```python
stopwords = {"the", "a", "an", "in", "on"}  # set，O(1) 查找
filtered = [w for w in words if w not in stopwords]
# 用 set 而不是 list，成员判断从 O(n) 变为 O(1)
```

**ASCII 柱状图**

```python
max_count = counter.most_common(1)[0][1]  # 最高词频
for word, count in counter.most_common(10):
    bar_len = count * 20 // max_count     # 等比缩放到 20 格
    bar = '#' * bar_len
    print(f"  {word:15s} {count:3d}  {bar}")
```

---

## Demo 3：链表实现

### C++ 指针思维 vs Python 对象引用

这是理解 Python 内存模型最好的例子：

```cpp
// C++：手动管理内存
struct Node {
    int val;
    Node* next;         // 原始指针，需要手动 delete
    Node(int v) : val(v), next(nullptr) {}
};
Node* head = new Node(1);
head->next = new Node(2);
// 用完必须 delete！否则内存泄漏
```

```python
# Python：GC 自动管理内存
class ListNode:
    def __init__(self, val=0):
        self.val  = val
        self.next = None   # 类型：Optional[ListNode]
                           # None 就是 nullptr，但 GC 自动回收

head = ListNode(1)
head.next = ListNode(2)
# 没有任何引用指向节点时，GC 自动回收——不需要 delete
```

### 删除节点：无需 `delete`

```python
def delete(self, val):
    if self.head.val == val:
        old = self.head
        self.head = self.head.next
        # old 现在没有任何引用指向它
        # GC 会自动回收 old 占用的内存
        # C++ 这里必须写 delete old;
        return True
    ...
    cur.next = cur.next.next   # 跳过要删除的节点，GC 自动回收
```

### 原地反转链表

经典算法，Python 写法更简洁（利用多重赋值）：

```python
def reverse(self):
    prev, cur = None, self.head
    while cur:
        # C++ 需要临时变量：Node* nxt = cur->next;
        # Python 利用元组赋值，一行完成三步
        cur.next, prev, cur = prev, cur, cur.next
        #   ↑ 右边先求值为 (prev, cur, cur.next)
        #   ↑ 再同时赋给左边三个变量
    self.head = prev
```

---

## Demo 4：任务调度器

### 装饰器 + 数据结构的结合

**`@task(name)` 装饰器**：给函数附加元数据并计时，这是 Python 元编程的典型用法：

```python
def task(name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            t0 = time.perf_counter()
            result = func(*args, **kwargs)
            print(f"[{name}] {(time.perf_counter()-t0)*1000:.1f}ms")
            return result
        wrapper.task_name = name   # 在函数对象上附加属性！
        return wrapper             # Python 函数是对象，可以有属性
    return decorator
```

**`collections.deque` 作为任务队列**

```python
from collections import deque

# deque = double-ended queue，类比 C++ std::deque
# append/popleft 都是 O(1)，比 list.pop(0) 的 O(n) 快得多
queue = deque()
queue.append(task1)     # 入队
queue.popleft()         # 出队 O(1)！
# list.pop(0) 是 O(n)，因为要移动所有元素
```

**`*args, **kwargs` 转发参数**

```python
class Scheduler:
    def submit(self, func, *args, **kwargs):
        # 把函数和它的参数一起存起来
        self.queue.append((func, args, kwargs))

    def run_all(self):
        while self.queue:
            func, args, kwargs = self.queue.popleft()
            func(*args, **kwargs)   # 展开参数调用
```

---

## 综合知识点回顾

| Demo | 核心技术 | 对应文档 |
|------|----------|----------|
| 成绩管理 | dataclass, property, sorted+key, statistics | DOC_02, DOC_03 |
| 词频分析 | Counter, re, set, 推导式 | DOC_02 |
| 链表 | 类, GC vs 手动内存, 多重赋值 | DOC_03 |
| 调度器 | 装饰器, deque, *args/**kwargs | DOC_02, DOC_04 |

---

## 扩展练习

1. **成绩管理**：添加 `export_csv()` 方法，用 `csv` 标准库把成绩写入文件
2. **词频分析**：支持分析本地 `.txt` 文件（用 `pathlib` 读取）
3. **链表**：实现 `__iter__` 让链表支持 `for x in ll:`，实现 `sorted_insert` 保持有序
4. **调度器**：添加优先级队列（用 `heapq` 标准库），高优先级任务先执行
