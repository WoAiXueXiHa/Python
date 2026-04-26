# # set 不保证顺序，想要排序用 sorted(s)

# # 1. 创建
# s1 = set()
# s2 = {1,2,3}
# s3 = set([1,2,2,3]) # 和 C++ 中的 set 一样，去重
# s4 = set("hello")
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# # 注意，这里的空 set 不能写 {} 因为 {} 是空 dict
# a = {}
# b = set()
# print(type(a))
# print(type(b))

# # 2. 增加元素
# s = set()
# s.add("app")
# s.add("mysql")
# s.add("cpp")
# s.add("mysql")
# print(s)

# # 3. 删除元素
# s = { "app", "cpp", "bpp"}
# s.remove("cpp")     # 元素不存在会报错
# print(s)
# s.discard("bpp")    # 元素不存在不会报错
# print(s)

# # 4. set 中没有索引，想要修改，先删除后添加
# s = { "app", "cpp", "bpp"}
# s.remove("cpp")
# s.add("java")
# print(s)

# # 5. 遍历
# s = {"app", "bpp", "cpp", "dpp"}
# for x in s:
#     print(x)

# # 顺序输出
# for x in sorted(s):
#     print(x)

# # 6. 常见方法
# a = {1,2,3}
# b = {3,4,5}
# print(a | b) # 并集
# print(a & b) # 交集
# print(a - b) # 差集 A - B
# print(a ^ b) # 对称差集 A∪B - A∩B

# 练习1. 输入
# map(函数, 列表) = 批量对每个元素执行函数 
# 这里 int 就是个函数，转成 int 类型
num = list(map(int, input().split()))
unique_num = set(num)
print(unique_num)

# 练习2. 输出交集
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(set(a) & set(b))

# 练习3. 
files = ["a.txt", "b.py", "a.txt"]
if len(files) != len(set(files)):
    print("has duplicate")
else:
    print("no duplicate")
