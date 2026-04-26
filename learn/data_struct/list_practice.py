# # 输入 n，再输入 n 个整数，
# # 存入列表，输出列表的最大值、最小值、总和。
# n = int(input("请输入一个数:"))
# a = []
# for i in range(0, n):
#     x = int(input())
#     a.append(x)
# print(max(a))
# print(min(a))
# print(sum(a))

# # 输入一行整数，用空格分隔，输出其中所有偶数。
# arr = list(map(int, input().split()))
# for i in arr:
#     if i % 2 == 0:
#         print(i, end=' ')


# 列表推导式
# new_list = [表达式 for 遍历 in 可迭代对象]
squares = [x * x for x in range(1,6)]
print(squares)

# 带条件过滤
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in nums if x % 2 == 0]
print(evens)

# 字符串处理
words = [" apple ", " banana ", " orange "]
clean_words = [word.strip() for word in words]
print(clean_words)

# 1. 生成 1 到 10 的平方列表
squares = [x*x for x in range(1,11)]
print(squares)

# 2. 输出所有偶数
nums = [1, 2, 3, 4, 5, 6]
ans = [x for x in nums if x % 2 == 0]
print(ans)

# 3. 生成所有 .py 文件列表
files = ["a.py", "b.txt", "c.py", "d.md"]
target = [file for file in files if file.endswith(".py")]
print(target)