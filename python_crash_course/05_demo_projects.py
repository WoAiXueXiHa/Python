# ============================================================
# Phase 5: 综合 Demo 项目
# ============================================================

# ══════════════════════════════════════════════════════════
# Demo 1: 学生成绩管理系统
# ══════════════════════════════════════════════════════════
from dataclasses import dataclass, field
from typing import List, Optional
import statistics

@dataclass
class Student:
    name:   str
    scores: List[float] = field(default_factory=list)

    def add_score(self, score: float):
        if not 0 <= score <= 100:
            raise ValueError(f"Score {score} out of range [0, 100]")
        self.scores.append(score)

    @property
    def average(self) -> Optional[float]:
        return statistics.mean(self.scores) if self.scores else None

    @property
    def grade(self) -> str:
        avg = self.average
        if avg is None: return "N/A"
        if avg >= 90:   return "A"
        if avg >= 80:   return "B"
        if avg >= 70:   return "C"
        if avg >= 60:   return "D"
        return "F"

    def __str__(self):
        return f"{self.name:10s} | avg={self.average:5.1f} | grade={self.grade}"


class GradeBook:
    def __init__(self, course: str):
        self.course   = course
        self.students: List[Student] = []

    def add_student(self, name: str) -> Student:
        s = Student(name)
        self.students.append(s)
        return s

    def top_students(self, n: int = 3) -> List[Student]:
        return sorted(
            [s for s in self.students if s.average is not None],
            key=lambda s: s.average,
            reverse=True
        )[:n]

    def class_stats(self):
        avgs = [s.average for s in self.students if s.average]
        if not avgs:
            return
        print(f"\n=== {self.course} Class Statistics ===")
        print(f"  Students : {len(self.students)}")
        print(f"  Class avg: {statistics.mean(avgs):.1f}")
        print(f"  Std dev  : {statistics.stdev(avgs):.1f}")
        print(f"  Highest  : {max(avgs):.1f}")
        print(f"  Lowest   : {min(avgs):.1f}")
        print(f"\n  {'Name':10s} | {'Avg':>5} | Grade")
        print(f"  {'-'*30}")
        for s in sorted(self.students, key=lambda x: x.average or 0, reverse=True):
            print(f"  {s}")


def demo_gradebook():
    gb = GradeBook("Python Programming")
    data = {
        "Alice":   [92, 88, 95, 91],
        "Bob":     [75, 82, 78, 80],
        "Charlie": [60, 55, 70, 65],
        "Diana":   [98, 95, 99, 97],
        "Eve":     [45, 50, 55, 48],
    }
    for name, scores in data.items():
        s = gb.add_student(name)
        for score in scores:
            s.add_score(score)

    gb.class_stats()
    print("\n  Top 3 students:")
    for i, s in enumerate(gb.top_students(3), 1):
        print(f"    {i}. {s}")


# ══════════════════════════════════════════════════════════
# Demo 2: 文本词频分析器
# ══════════════════════════════════════════════════════════
from collections import Counter
import re

def word_frequency(text: str, top_n: int = 10):
    """统计文本中词频，返回 top_n 个高频词"""
    words    = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    stopwords = {"the", "a", "an", "in", "on", "at", "to", "of", "and", "or",
                 "is", "was", "are", "were", "be", "been", "it", "this", "that"}
    filtered = [w for w in words if w not in stopwords]
    counter  = Counter(filtered)

    print(f"\n=== Word Frequency (top {top_n}) ===")
    print(f"  Total words  : {len(words)}")
    print(f"  Unique words : {len(counter)}")
    print(f"  Top {top_n}:")
    for word, count in counter.most_common(top_n):
        bar = '#' * (count * 20 // (counter.most_common(1)[0][1]))
        print(f"    {word:15s} {count:3d}  {bar}")
    return counter


def demo_word_freq():
    text = """
    Python is a high-level programming language known for its simplicity and readability.
    Python supports multiple programming paradigms including procedural, object-oriented,
    and functional programming. Python has a large standard library and a vibrant community.
    Many developers choose Python for data science, machine learning, web development,
    and scripting. Python code is often more concise than equivalent code in other languages.
    """
    word_frequency(text, top_n=8)


# ══════════════════════════════════════════════════════════
# Demo 3: 简单链表实现（对比 C++ 指针思维）
# ══════════════════════════════════════════════════════════
# C++: struct Node { int val; Node* next; };
# Python: 用对象引用替代指针，GC 自动管理内存！

class ListNode:
    def __init__(self, val=0):
        self.val  = val
        self.next: Optional['ListNode'] = None  # 用类型提示替代 Node*


class LinkedList:
    def __init__(self):
        self.head: Optional[ListNode] = None
        self._size = 0

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        self._size += 1

    def prepend(self, val):
        new_node  = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def delete(self, val) -> bool:
        if not self.head:
            return False
        if self.head.val == val:
            self.head = self.head.next   # GC 自动回收旧头节点（不需要 delete）
            self._size -= 1
            return True
        cur = self.head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next # GC 自动回收
                self._size -= 1
                return True
            cur = cur.next
        return False

    def to_list(self) -> list:
        result, cur = [], self.head
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result

    def reverse(self):
        """原地反转链表"""
        prev, cur = None, self.head
        while cur:
            nxt       = cur.next
            cur.next  = prev
            prev, cur = cur, nxt
        self.head = prev

    def __len__(self):  return self._size
    def __str__(self):  return " -> ".join(map(str, self.to_list())) + " -> None"


def demo_linked_list():
    ll = LinkedList()
    for v in [1, 2, 3, 4, 5]:
        ll.append(v)
    print(f"\n=== Linked List ===")
    print(f"  Initial  : {ll}")
    ll.prepend(0)
    print(f"  Prepend 0: {ll}")
    ll.delete(3)
    print(f"  Delete  3: {ll}")
    ll.reverse()
    print(f"  Reversed : {ll}")
    print(f"  Length   : {len(ll)}")


# ══════════════════════════════════════════════════════════
# Demo 4: 迷你任务调度器（生成器 + 装饰器组合）
# ══════════════════════════════════════════════════════════
import time
import functools
from collections import deque

def task(name):
    """装饰器：将函数标记为任务并记录执行时间"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            t0 = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - t0
            print(f"  [Task:{name:12s}] done in {elapsed*1000:.1f}ms -> {result}")
            return result
        wrapper.task_name = name
        return wrapper
    return decorator


class Scheduler:
    def __init__(self):
        self.queue: deque = deque()

    def submit(self, func, *args, **kwargs):
        self.queue.append((func, args, kwargs))

    def run_all(self):
        print(f"\n=== Scheduler: {len(self.queue)} tasks ===")
        results = []
        while self.queue:
            func, args, kwargs = self.queue.popleft()
            results.append(func(*args, **kwargs))
        return results


@task("fibonacci")
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@task("sum_squares")
def sum_squares(n):
    return sum(x**2 for x in range(n))

@task("word_count")
def word_count(text):
    return len(text.split())


def demo_scheduler():
    sc = Scheduler()
    sc.submit(fib, 30)
    sc.submit(fib, 50)
    sc.submit(sum_squares, 10_000)
    sc.submit(word_count, "Python is great for rapid development")
    sc.run_all()


# ══════════════════════════════════════════════════════════
# 主入口
# ══════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 50)
    print(" DEMO 1: Grade Book")
    print("=" * 50)
    demo_gradebook()

    print("\n" + "=" * 50)
    print(" DEMO 2: Word Frequency")
    print("=" * 50)
    demo_word_freq()

    print("\n" + "=" * 50)
    print(" DEMO 3: Linked List")
    print("=" * 50)
    demo_linked_list()

    print("\n" + "=" * 50)
    print(" DEMO 4: Task Scheduler")
    print("=" * 50)
    demo_scheduler()
