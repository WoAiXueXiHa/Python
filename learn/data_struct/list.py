# list 很像 vector
# 但是 list 可以存放不同的类型数据，支持切片

# 1. 创建方式
from audioop import reverse
import re


a = [1, 2, "ss", 3.14, True, 4, 5]
b = []
c = list()
d = list("abc")
print(a)
print(b)
print(c)
print(d)

# 2. 增加元素
a = [1, 2, 3]
a.append(4)     # 尾插一个元素，这个元素可以是任何类型
a.append("hel")
a.append([5,6])
print(a)

a.insert(0,20)  # 指定位置插入，超过数组大小就是尾插
print(a)

b = [3,2,1]
a.extend([100,200])  # 追加另一个列表的所有元素
print(a)
b.extend(a)
print(b)

# 3. 删除元素
a = [10,20,30,40,50]
x = a.pop()  # 默认删除最后一个元素
print(x)
print(a)

y = a.pop(1)  # 指定位置删除
print(y) 
print(a)

a.remove(30)  # 删除第一个匹配的元素，找不到会报错
print(a)

# del a[i] # 删除索引为i的元素
del a[1]
print(a)

# 4. 遍历方式
a = [5,4,3,2,1]
# 带索引推荐这种方式
for i, x in enumerate(a):
    print(i, x)

# 5. 常用的方法
a = [1,21,7,14,5,3]
print(len(a))  # 元素个数
print(max(a))  # 最大值
print(min(a))  # 最小值

b = list("defgabd")
print(b.count('e'))  # 元素e出现的次数
print(b.index('f'))  # 查找元素f的第一次出现的位置
b.reverse()   # 原地反转
print(b)
b.sort()  # 原地排序
print(b)
