# # # 定义一个类
# # class Dog:
# #     # self 就是 this 指针 self要显式存在
# #     def bark(self):
# #         print("wnagwang")
# # # 创建对象
# # d = Dog()
# # d.bark()

# # # 构造函数
# # class Cat:
# #     def __init__(self, name):
# #         self.name = name
# # # 创建对象
# # c = Cat("喵喵")
# # print(c.name)

# # # 成员函数
# # class Cat:
# #     def __init__(self, name):
# #         # 成员变量直接在__init__里赋值
# #         self.name = name
    
# #     def bark(self):
# #         print(f"{self.name} 在喵喵叫")
# # c = Cat("喵喵")
# # c.bark()

# # class PromptBuilder:
# #     def __init__(self, role):
# #         self.role = role
    
# #     def build(self, question):
# #         return f"你是{self.role}。\n请回答：{question}"
# # builder = PromptBuilder("Python老师")
# # prompt = builder.build("什么是字典？")
# # print(prompt)

# # self 就是当前对象本身
# # self.xxx 就是当前对象的成员变量/属性
# class Stu:
#     def __init__(self, name, age):
#         # 想要什么成员变量，初始化时传参赋值就行
#         self.name = name
#         self.age = age
    
#     def introduce(self):
#         print(f"我叫{self.name}，今年{self.age}岁")
# stu = Stu("kunkun", 25)
# stu.introduce()

# class Counter:
#     def __init__(self, val):
#         self.val = 0

#     def inc(self):
#         self.val += 1

#     def show(self):
#         print(self.val)

# class PromptBuilder:
#     def __init__(self, role):
#         self.role = role
    
#     def build(self, question):
#         return f"我是{self.role}\n{question}"
# builder = PromptBuilder("Python助教")
# print(builder.build("什么是函数？"))


class PromptBuilder:
    def __init__(self, role):
        self.role = role
    
    def build(self, question):
        return f"你是{self.role}。\n用户问题：{question}"

def main():
    try:
        role = input("请输入角色: ")
        question = input("请输入问题: ")
    
        bulider = PromptBuilder(role)
        prompt = bulider.build(question)

        print("生成的 Prompt: ")
        print(prompt)

    except Exception as e:
        print(f"程序出错: {e}")
    
if __name__ == "__main__":
    main()

