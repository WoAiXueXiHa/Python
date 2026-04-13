def info_qa():
    name = input("请输入用户名：")
    try:
        age = int(input("请输入年龄"))
        if age < 18:
            print(f"你好，{name}， 你还未成年")
        else:
            print(f"你好，{name}，你已经成年")
        
        print(f"明年你{age + 1} 岁")
    except Exception as e:
        print(f"输入数字不合法: {e}")


def sta():
    try:
        num = int(input("请输入一个正整数: "))
    except ValueError:
        print("输入不合法")
        return
    cur = 1
    even = 0
    odd = 0
    even_sum = 0
    odd_sum = 0
    while cur <= num:
        if cur % 2 == 0:
            even += 1
            even_sum += cur
        else:
            odd += 1
            odd_sum += cur
        cur += 1
    print(f"1~{num}中偶数有{even}个")
    print(f"1~{num}中奇数有{odd}个")
    print(f"1~{num}中偶数和为{even_sum}")
    print(f"1~{num}中奇数和为{odd_sum}")


def sta_str():
    text = input("请输入一个字符串: ")
    cur = {}

    for c in text:
        if c not in cur:
            cur[c] = 1
        else:
            cur[c] += 1
    
    for key, value in cur.items():
        print(key, value)

def main():
    info_qa()
    sta_str()
    sta()

if __name__ == "__main__":
    main()
