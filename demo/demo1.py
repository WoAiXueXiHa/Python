# ---------------------- 数据类型 --------------------
# 基础类型
"""
文档字符串
区域注释
"""
# 1. 整数型 int
a = 10
print(type(a))
print(a)
# 2. 浮点型 float
b = 3.14
print(type(b))
print(b)
# 3. 字符串型 str
cc = 'hello'    # '' "" 这两种都是字符串
c = "hello world"
print(type(cc))
print(cc + c)    # 字符串拼接
# python是左闭右开的，即[0, len(c))
print("c[0]: ", c[0])       # 字符串索引,第一个元素
print("c[-1]: ", c[-1])      # 字符串索引，最后一个元素

print("c[0:5]: ", c[0:5])     # 字符串切片，第0到第四个元素
print("c[0:5:2]: ", c[0:5:2])   # 字符串切片，每隔2个取一个元素 
print("c[:2]: ", c[:2])      # 字符串切片，从头到第2个元素
print("c[2:]: ", c[2:])      # 字符串切片，从第2个元素到末尾

print("len(c): ", len(c))     # 字符串长度  
print("c.upper(): ", c.upper())  # 字符串大写
print("c.lower(): ", c.lower())  # 字符串小写
print("c.replace('l', 'L'): ", c.replace('l', 'L'))  # 字符串替换

# 4. 布尔型 bool
is_true = True
is_false = False
print(type(is_true))
print(is_true)
print(type(is_false))
print(is_false)
# 5. 空值 None
d = None
print(type(d))
print(d)

# ---------------------- 格式化输出 ----------------
num = 0
# input() 返回的是个字符串
num = int(input("请输入一个数字："))
print("你输入的数字是：", num)

val = 1
# f: 前缀的字符串，后面跟着的变量会被格式化输出
# 可以用{}内嵌其它变量和表达式 
print(f"The value is {val}")
print(f'num: {num}, val: {val}, num + val: {num + val}')
print("---------------------------------------------")
print("---------------------------------------------")

# ---------------------- 运算符 --------------------
# 1. 算术运算符
a = 10
b = 3
c = 777
print(a + b)
print(a - b)
print(a * b)
print(a / b)    # 浮点数结果
print(a // b)   # 取整除，和cpp的/相同
print(a % b)    # 取余
print(a ** b)   # 幂运算

# 关系运算符同cpp
# 逻辑运算符同cpp
print(a < b and b < a)  # &&
print(a < b or b < a)   # ||
print(not a < b)        # !

# 交换两个变量
val = 10
temp = 20
print(val, temp)
val, temp = temp, val
print(val, temp)
# 位运算符同cpp