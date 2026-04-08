# 1. 变量定义，Python不写类型，没有;
a = 10
b = 2.4
str = "Hello, World!"
# Python 变量名没有固定类型，可以随时改变
a = "Hello, World!"
print(a)
# 但是，不能类型不匹配
# 1 + "1" 会报错


# 2. 四个单位一个缩进，同一缩进就是同一代码块
# :冒号开始代码块
if a > 10:
    print("a is greater than 10")
else:
    print("a is less than 10")

# 3. 输入输出简单
x = input("Enter a number: ")  # 一定注意，input返回的是字符串
print(x)
x = int(input("Enter a number: "))
print(x)

# 4. 基础数据类型 int float bool str
# 容器类型
# 4.1. list 类似vector
nums = [1,2,3] # 数组用[]包围
nums.append(4) # 追加元素
# 切片 [begin:end:step] [开始,结束)step是步长，左闭右开，和迭代器一样
# 支持逆序
# 10 20 30 40 50
# 0  1  2  3  4  
# -5 -4 -3 -2 -1
arr = [10,20,30,40,50]
print(arr[0:3:2]) # [10,30]
print(arr[::-1]) # [50,40,30,20,10]
print(arr[::2]) # [10,30,50]
print(arr[1::2]) # [20,40]

