# 字典 dict 对应 unordered_map
'''
unordered_map<string,int> cnt;
cnt["cpp"] = 3;
cnt["python"] = 1;
'''
cnt = {}
cnt["cpp"] = 3
cnt["python"] = 1

# unordered_map 访问不存在的 key 会自动插入默认值
# dict 访问不存在的 key 会报错 -> 为了安全访问，用 get(key, 0)

# 1. 创建
d1 = {}
d2 = dict()
d3 = {
    "apple" : 3,
    "banana" : 5
}
d4 = dict(apple=3, banana=5)

print(d1)
print(d2)
print(d3)
print(d4)

# 2. 增加
score = {}
score["Alice"] = 85
score["Bob"] = 80

print(score)

# 3. 修改
score["Alice"] = 90
print(score)

# 4. 查找
print(score["Alice"])
print(score.get("Bob"))
print(score.get("Charlie", 0))

# 判断 key 是否存在
if "Alice" in score:
    print("Alice is in the score dictionary.")
else:
    print("Alice is not in the score dictionary.")

# 5. 删除
del score["Bob"]
print(score)
# 用 pop 如果 key 不存在会报错，给默认值就好
score.pop("Alice")
x = score.pop("Charlie",0)
print(x)
print(score)

# 6. 遍历
scores = {
    "niuniu" : 80,
    "huanhuan" : 90,
    "qiangqing" : 100,
    "lele" : 80
}
# 遍历 key 二者等价
for name in scores:
    print(name)
for name in scores.keys():
    print(name)

# 遍历 value
for score in scores.values():
    print(score)

# 遍历 key-value 
for name, score in scores.items():
    print(name, score)
'''
for(auto& [key, value] : mp) cout << key << ":" << value << endl;
'''

# 7. 合并另一个字典
d = {
    "a" : 1,
    "b" : 2
}
d.update(
    {
        "c" : 3,
        "a" : 101   # 会覆盖旧值
    }
)
print(d)

# 8. 用途
# 计数模板
cnt = {}
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
for word in words:
    cnt[word] = cnt.get(word, 0) + 1
print(cnt)