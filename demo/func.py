def add(a,b):
    return a + b
# 定义方式轻量化

# 类型注释
# 这和C++就没啥区别了，写这个，符合C++习惯
def mul(a:int, b:int) -> int :
    return a * b

# 参数传递：直接把对象引用传给形参，不像C++细化那么多
def f(x):
    x.append(4)
a = [1,2,3]
f(a)
print(a)
# 这是可变对象，效果就是引用传递

# 对于不可变对象，效果就是值传递
def func(x):
    x = x + 1 # 没有++ --
a = 10
func(a)
print(a)

# 缺省参数
# C++ 半缺省，只能右->左设置，不能跳跃
def greet(name, msg="hello"):
    print(msg, name)

greet("kunkun")
greet("kunkun", "Hi")

# 看个例子
def add_item(x, lst=[]):
    lst.append(x)
    return lst

print(add_item(1))
print(add_item(2))
print(add_item(3))

# Python的缺省参数是：在函数定义时创建一次，不是每次调用重新创建，[]被复用了
# 如果不想复用，这样写
def add_item_2(x, lst = None):
    if lst is None:             # None是不可变、稳定得值，用来表示用户没传
        lst = []
    lst.append(x)
    return lst

def con(host, port, timeout):
    print(host, port, timeout)

# 和C++一样，按顺序
con("local", 2808, 5)
# 关键字参数，可以换顺序
con(timeout=5, host="local", port=2808)


# 可变参数*args
def total(*args):
    print(args) 
    return sum(args)

print(total(1,2,3,4,5)) 
# (1,2,3,4,5)\n15
# *args会把多余的位置参数收集成一个tuple

# 可变参数**kwargs
def show_info(**kwargs):
    print(kwargs)
show_info(name="kun", age=25, city="Beijing")
# **kwargs会把多余得关键字参数手机成一个哈希表

def func(a, b, *args, **kwargs):
    print(a,b)
    print(args)
    print(kwargs)

func(1,2,3,4,x=10,y=30)



