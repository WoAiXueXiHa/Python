# 输入 n，再输入 n 个整数，
# 存入列表，输出列表的最大值、最小值、总和。
n = int(input("请输入一个数:"))
a = []
for i in range(0, n):
    x = int(input())
    a.append(x)
print(max(a))
print(min(a))
print(sum(a))

# 输入一行整数，用空格分隔，输出其中所有偶数。
arr = list(map(int, input().split()))
for i in arr:
    if i % 2 == 0:
        print(i, end=' ')