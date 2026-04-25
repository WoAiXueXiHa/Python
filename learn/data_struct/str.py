'''
字符串是不可变对象
s = "hello world"
s[0] = 'H' # TypeError: 'str' object does not support item assignment
'''
# 必须要创建新的字符串
s = "hello world"
# [start:end:step]
s = "H" + s[1:]
print(s)


# 1. 创建方式
s1 = "hello"
s2 = 'hello'
s3 = """multi,
line,
string"""
print(s1)
print(s2)
print(s3)

# 2. 查询操作
# 支持正序和倒序
#   P   y   t   h   o   n
#   0   1   2   3   4   5
#  -6  -5  -4  -3  -2  -1
s = "Python"
print(s[0]) # P
print(s[1:4]) # yth
print(s[::2]) # Pyto
print(s[-1])   # n
print(s[::-1]) # nohtyP

# 3. 常用方法
s = "   hello world    "
print(s.strip())    # 去除两端空格
print(s.upper())
print(s.lower())
print(s.replace("python", "C++"))
print(s.split())    # 按照空白切割 split(",") 这就是按照逗号切割
print("hello" in s)
print(s.find("l"))  # 找到第一个l的位置
print(s.count("l")) # 统计l出现的次数
print(s.startswith("h")) # 是否以h开头
print(s.endswith("d"))   # 是否以d结尾
print("sep".join(["w", "o", "r", "l", "d"])) # 用分隔符拼接字符串列表

# 4. 遍历方法
s = "abs"
for ch in s:
    print(ch)
# 带索引
for i, ch in enumerate(s):
    print(i, ch)