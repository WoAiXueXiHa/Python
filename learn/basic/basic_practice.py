# 1. 输出个人信息
name = "Vect"
age = 21
print(f"hello, {name}. You are {age} years old.")

# 2. 输出1 ~ n 的和
num = int(input("请输入一个数字: "))
sum = 1
i = 1
while i <= num:
    sum += i
    i += 1
print(f"1 ~ {num}数字之和为：{sum}")

# 3. 输出 1 ~ n 的所有偶数
cnt = int(input("请输入一个数字: "))
for i in range(1, cnt+1, 2):
    print(i)

# 4. 猜数字，答案固定为 ans = 7
guess = int(input("请输入一个数字进行猜测:"))
while True:
    if guess < 7:
        guess = int(input("猜小了，再试一次:"))
    elif guess > 7:
        guess = int(input("猜大了，再试一次:"))
    else:
        print("恭喜你猜对了！")
        break

# 5. 输出乘法口诀表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i} x {j} = {i*j}", end="  ")
    print()

    
