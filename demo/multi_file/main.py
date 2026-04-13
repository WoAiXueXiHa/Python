# # 导入一个模块中的某个名字
# from my_math import add
# print(add(6,10))

# # 导入整个模块
# import my_math
# print(my_math.add(4,4))
# print(my_math.sub(4,4))
# print(my_math.div(4,4))
# print(my_math.mul(4,4))

# # 起别名
# import my_math as hh
# print(hh.add(4,4))
# print(hh.sub(4,4))
# print(hh.div(4,4))
# print(hh.mul(4,4))


# 函数的入口
def main():
    print("main函数")

# 当这个文件直接运行时，执行main()
# 如果这个文件被别的文件导入，就不执行
# 这是一种文件入口的保护机制
if __name__ == "__main__":
    main()



