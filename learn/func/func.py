# learn/func/func.py

def greet(name):
    return f"你好, {name}!"

def add_numbers(a, b):
    return a + b

def is_even(number):
    return number % 2 == 0

if __name__ == "__main__":
    print(greet("小明"))
    print(add_numbers(3, 5))
    print(is_even(4))
    print(is_even(7))
