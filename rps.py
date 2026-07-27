import random

# 用列表存三个选项
choices = ["石头", "剪刀", "布"]

# 电脑随机选一个
computer = random.choice(choices)

# 玩家输入
player = input("你出什么（石头/剪刀/布）：")

# 显示双方出什么
print("电脑出了：", computer)
print("你出了：", player)

# 判断输赢
if player == computer:
    print("平局！")
elif (player == "石头" and computer == "剪刀") or \
     (player == "剪刀" and computer == "布") or \
     (player == "布" and computer == "石头"):
    print("你赢了！")
else:
    print("你输了！")