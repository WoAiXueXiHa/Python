# # 不强制写类型和返回参数
# def add(a,b):
#     return a + b

# ans = add(6,4)
# print(ans)

# # 没有返回值，默认返回None
# def greet(name):
#     print(f"hhh, {name}")
# name = "huhhu"
# result = greet(name)
# print(result)

# # 缺省参数
# def greet(name, msg = "你好"):
#     print(f"{msg}, {name}")
# greet("kunkun")
# greet("kunkun","hahah")

# # 关键字参数，调用函数时写参数名
# def introduce(name, age):
#     print(f"我叫{name}，今年{age}岁")

# # 顺序无所谓
# introduce(name="aaa",age=20)
# introduce(age=20,name="aaa")

# # 返回多个值
# def get_user():
#     return "kun", 20, "A"
# name, age, degree = get_user()
# print(name)
# print(age)
# print(degree)
# # 本质上返回一个tuple

# # 类型注解
# # 这些类型这是建议
# def add(a:int, b:int) -> int:
#     return a + b
# print(add(3.14, 7.2))

# # 把统计次数封装成函数
# def count_words(words):
#     ans = {}
#     for word in words:
#         if word not in ans:
#             ans[word] = 1
#         else:
#             ans[word] += 1
#     return ans

# data = ["ai", "python", "ai", "langchain", "python", "ai"]
# print(count_words(data))

# demo1 
def add(a,b):
    print(a + b)
add(20,333)

# demo2
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(17))
print(is_even(16))

# demo3
def count_words(words):
    ans = {}
    for word in words:
        if word not in ans:
            ans[word] = 1
        else:
            ans[word] += 1
    return ans

data = ["ai", "python", "ai", "langchain", "python", "ai"]
print(count_words(data))

# demo4
def greet(name, msg="你好"):
    print(name,msg)
greet(name="kunkun",msg="hhhh")
greet("kunkun")
