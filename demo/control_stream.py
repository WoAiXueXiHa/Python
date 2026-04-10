# # 条件判断
# # if elif else

# # :加上四个缩进是同一个{}括起来
# # 条件没有括号
# num = 10
# if num >= 10:
#     print("Yes")
#     print("四个缩进")
# print("这就不是四个缩进了，我已经跳出了判断")

# score = 90
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# else:
#     print("C")

# # && 在python里成了 and

# age = 18
# has_ticket = True
# if age >= 18 and has_ticket:
#     print("可以进入")
# else:
#     print("不能进入")

# # 对象也能放入条件判断
# name = ""
# if name:
#     print("有内容")
# else:
#     print("无内容")

# # 常见的假值： False None 0 0.0 "" [] () 

# # 支持链式比较
# val = 20
# if 10 <= val <= 30:
#     print("在这个范围")

# # demo1: 输入年龄，判断年龄区间
# age = int(input("请输入一个年龄："))

# if 0 <= age < 18:
#     print("未成年，小屁孩")
# elif 18 <= age <= 30:
#     print("成年了，青年")
# elif 31 <= age <= 55:
#     print("成年了，壮年")
# elif 56 <= age <= 120:
#     print("老年")
# else:
#     print("输入不合法，请重新输入")


# # range(begin,end,step) 左闭右开，和迭代器一样
# for i in range(0,100,3):
#     print(i)

# name = "Python"
# for ch in name:
#     print(ch)

# cnt = 10
# while cnt >  5:
#     print(cnt)
#     cnt -= 1

# demo2: 打印1~100的偶数
for i in range(2, 101, 2):
    if i % 2 == 0:
        print(i)

# # demo3: 输入一个n，计算1+2+..+n
# num = int(input("请输入一个正整数："))
# sum = 0
# i = 1
# while i <= num:
#     sum += i
#     i += 1
# print(f"最后的结果是:{sum}")


