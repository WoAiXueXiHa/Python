# # list 像vector一样
# nums = [10,20,30]
# # 能存不同的类型
# mul_set = [1,2,3,"jjjj",3.14,[12]]
# for i in mul_set:
#     print(i)
# # 可以拿到索引
# for i in range(len(mul_set)):
#     print(i, mul_set[i])

# # tuple ()包围的数据 不可以修改的有序序列 固定记录 轻量只读
# point = (10,20)

# def get_user():
#     return "kunkun",2.5
# name, age = get_user()

# # dict 类似map
# user = {
#     "name" : "kunkun",
#     "age"  : "2.5"
# }
# user["city"] = "Beijing"

# config = {
#     "model": "gpt-4",
#     "temperature": 0.7,
#     "stream": True
# }
# for key in config:
#     print(key, config[key])
# for key, value in config.items():
#     print(key, value)

# # set 无序去重集合 去重，快速判断某元素是否存在
# s = {1,2,3}
# s.add(4)
# print(s)

# nums = [1,2,3,4,4,6,8,8,9]
# unique_nums = set(nums)
# print(unique_nums)

# demo1
nums = [1,2,3,4,5]
print(nums[0])
nums.append(6)
for i in nums:
    print(i)

# demo2
user = {
    "name": "Alice",
    "age": 20
}
print(user["name"])
user["city"] = "Shanghai"
for key, value in user.items():
    print(key, value)

# demo3：统计单词出现次数
words = ["ai", "python", "ai", "langchain", "python", "ai"]
ans = {}
for word in words:
    if word in ans:
        ans[word] += 1
    else:
        ans[word] = 1
print(ans)
