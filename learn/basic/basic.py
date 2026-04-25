# 1. 变量和类型
'''
int age = 10;
double price = 9.99;
string name = "John";
bool isStudent = true;
'''
# python写法：
age = 10
price = 9.99
name = "John"
isStudent = True
# 查看变量类型
x = 20
print(type(age))
print(type(price))
print(type(name))
print(type(isStudent))


# 注意：字符串和数字不能直接相加
age = 30
print("age = " + str(age))

# 2. 输入输出
# 输出print，print可以输出多个值，默认空格分隔
print("hhhhhhh")
print(123)
print("age =", 12)
# 格式化输出 f-string
name = 'Vect'
age = 21
print(f"my name is {name}, and I am {age} years old.")

# 输入input，input()读入并返回的是字符串
num = int(input("请输入一个数字："))
print(f"你输入的数字+1是:{num + 1}")

# 3. if-else
'''
if 条件:
    代码块
elif 条件:
    代码块
else:
    代码块
'''
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")

'''
注意逻辑运算符
&& and
! not
|| or
'''
if score >= 90 and score <= 100:
    print("优秀")
elif score >= 80 and score < 90:
    print("良好")
elif score >= 70 and score < 80:
    print("及格")
else:
    print("不及格") 

# 4. for循环
'''
for 变量 in 序列:
    代码块
'''
for i in range(1, 11):
    print(i)

arr = [10,20,30]
for x in arr:
    print(x)
str = "hello,python"
for ch in str:
    print(ch)

# 5. while循环
'''
while 条件:
    代码块
'''
i = 0
while i < 10:
    print(i)
    i += 1

num = 0
while num < 10:
    num += 1
    if num == 3:
        continue
    if num == 6:
        break
    print(num)


# 6. range() 生成一个整数序列
# [1,10] 和迭代器一样 左闭右开区间
for i in range(1, 11):
    print(i)

# range(start,stop,step)
for i in range(0,8,2):
    print(i)
# 倒序 for(int i = 7; i >= 0; i--)
for i in range(7, -1, -1):
    print(i)




