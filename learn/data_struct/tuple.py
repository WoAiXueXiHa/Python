# tuple 是一个不可修改的固定数组 元组
# 1. 创建
from os import name


t1 = (1,2,3)
t2 = ()
t3 = tuple([1,2,3])
t4 = ("Alice", 20)
print(t1)
print(t2)
print(t3)
print(t4)
# 注意：单个元素的元组必须加逗号
a = (1)
b = (1,)
print(type(a))
print(type(b))

# 2.常用方法 
t = (1,3,4,5,6)
print(t.count(3))
print(t.index(1))

# 3.元组解包->主要用于函数返回多个值
t = (1,2,3)
x,y,z = t
print(x,y,z)

# 练习
# 1. 定义一个元组保存二维点坐标 (3, 4)，分别输出 x 和 y
pos = (3, 4)
x,y = pos
print(x,y)

# 2.用解包方式输出姓名、年龄、城市。
person = ("Tom", 18, "Shanghai")
name, age, city = person
print(f"{name} is {age} years old, from {city}")

# 3. 统计元组中数字 2 出现的次数：
nums = (1, 2, 3, 2, 4, 2)
print(nums.count(2))