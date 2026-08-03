def 加法(a, b):
 return a + b

def 减法(a, b):
 return a - b

def 乘法(a, b):
 return a * b

def 除法(a, b):
 return a / b

# 主程序
print("=== 简易计算器 ===")
print("1. 加法")
print("2. 减法")
print("3. 乘法")
print("4. 除法")

选择 = input("请选择功能（1-4）：")
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))

if 选择 == "1":
 结果 = 加法(num1, num2)
 print(num1, "+", num2, "=", 结果)
elif 选择 == "2":
 结果 = 减法(num1, num2)
 print(num1, "-", num2, "=", 结果)
elif 选择 == "3":
 结果 = 乘法(num1, num2)
 print(num1, "×", num2, "=", 结果)
elif 选择 == "4":
 结果 = 除法(num1, num2)
 print(num1, "÷", num2, "=", 结果)
else:
 print("输入错误！")
 结果 = round(结果, 2)  # 保留2位小数