# 1.
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
cnt = {}
for word in words:
    cnt[word] = cnt.get(word, 0) + 1
print(cnt)

# 2.输入 n，再输入 n 个姓名和成绩，保存到字典中，
# 最后输入一个姓名，输出该人的成绩。如果不存在，输出 not found。
num = int(input("请输入一个数字:"))
i = 0
cnt = {}
while i < num:
    name = input("name = ")
    score = int(input("score = "))
    cnt[name] = score
    i += 1

find = input("要找的人的姓名:")
if find in cnt:
    print(cnt[find])
else:
    print("找不到这个人")

# 3. 输出所有分数大于等于 80 的人名
scores = {"Alice": 90, "Bob": 85, "Tom": 70}
for name in scores:
    if scores[name] >= 80:
        print(name)
