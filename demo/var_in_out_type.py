# # Python 里不用先写类型 直接赋值
# x = 10
# y = "hello"
# z = True

# print(x,y,z)

# name = input("输入一个数字：") # input返回的是字符串
# print(int(name) + 20)

# # 字符串格式化
# size = 10
# type = "hhh"
# # 相当于是C++拼接输入，并且支持格式化
# print(f"type是{type}, size是{size}")


# # demo1: 写一个程序，输入基本信息
# name = input("输入你的名字:")
# age = int(input("输入你的年龄:"))
# print(f"我叫{name},今年{age}岁")

# # type()函数查看类型
# a = 10
# b = 3.14
# c = "python"
# d = True
# e = None
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# # python 强调 x 只是一个名字 可以绑定到任何类型对象
# # 10 是 整数对象  "hhhhh"是字符串对象
# x = 10 
# print(type(x))
# x = "hhhhh"
# print(type(x))

# # 向下取整除法
# print(10 // 3)  # 3
# print(-10 // 3) # -4

# # 字符串操作
# name = "python"
# print(name.upper())
# print(name.lower())
# print(len(name))
# print(name[0])
# print(name[-1])

# is_ok = True
# is_done = False

# print(is_ok)
# print(not is_ok)
# print(is_ok and is_done)
# print(is_ok or is_done)


# demo2：定义五个不同类型变量，分别打印值，类型
a = 10
b = 3.14
c = "12345"
is_ok = True
null = None

print(a)
print(b)
print(c)
print(is_ok)
print(null)

print(type(a))
print(type(b))
print(type(c))
print(type(is_ok))
print(type(null))

print(a + b)
print(len(c))
print(c[0])
print(not is_ok) # 取反 not