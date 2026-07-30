# 定义一个函数：打招呼
def say_hello():
    print("你好！")
    print("欢迎学习Python！")

# 调用函数
say_hello()
say_hello()
say_hello()

print("---")

# 带参数的函数：可以传入不同的名字
def greet(name):
    print("你好，" + name + "！")

# 调用函数，传入不同的名字
greet("潘江波")
greet("小明")
greet("小红")

print("---")

# 带返回值的函数：计算后返回结果
def add(a, b):
    result = a + b
    return result

# 调用函数，把结果存到变量里
total = add(5, 3)
print("5 + 3 =", total)

total2 = add(10, 20)
print("10 + 20 =", total2)