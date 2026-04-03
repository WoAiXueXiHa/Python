# 1. 字符串和 f-string
from zlib import MAX_WBITS


name = "Alice"
age = 25
city = "Beijing"
print(f"{name} 今年 {age} 岁，来自 {city}")
print(f"{name} 的名字长度是 {len(name)}")
print(name.upper())


# 2. 列表循环
scores = [85, 92, 88, 95]
print("成绩:")
for i in scores:
    print(i)

total = 0
for j in scores:
    total += j
print("总分:",total)

print(f"平均分: {total / len(scores) : .1f}")

# 列表操作
numbers = [3, 7, 2, 9, 1, 5, 8, 4, 6]
big_nums = []
small_nums = []
for i in numbers:
    if(i > 5):
        big_nums.append(i)
    else:
        small_nums.append(i)

print(f"大于 5 的数字: {big_nums}")
print(f"小于等于 5 的数字: {small_nums}")
print(f"small_nums的长度: {len(small_nums)}; big_nums的长度: {len(big_nums)}")
print()

# 字典
student = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88,
    "Eve": 95
}
for key,value in student.items():
    print(f"{key}:{value}")

max = 0
min = 100
max_name = ""
min_name = ""
total = 0
# 这里就固定死了 name就是key，score就是value
for name,score in student.items():
    total += value
    if score > max:
        max = score
        max_name = name
    if score < min:
        min = score
        min_name = name

print(f"成绩最高:{max_name}:{max}")
print(f"成绩最低:{min_name}:{min}")
print(f"平均成绩: {total / len(student) : .1f}")


