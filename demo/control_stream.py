# if-else 不能有()
x = 10
if x >= 10:
    print("Y")
else:
    print("N")

y = 10 
if y > 10:
    print("1")
elif y == 10:
    print("2")
else:
    print("3")


# for 循环
# range() 生成整数序列的工具
# range(begin, end, step) 还是左闭右开
for i in range(0,20,3):
    print(i)

# enumerate() 索引和值一块拿
arr = [10,9,8,7,6,5]
for i, x in enumerate(arr):
    print(i,x)

# for-else
target = 10
for x in range(0,80,3):
    if x == target:
        print("found")
        break
else:   # 循环正常结束，没有被break打断，才执行else
    print("not found")

# while
n = 10
i = 0
while i <= n :
    print(i)
    i += 1

