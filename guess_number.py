import random

secret = random.randint(1, 100)
print("猜数字游戏开始！我心里想了一个1到100之间的数字。")

guessed = False

while guessed == False:
    guess = int(input("你猜是多少："))
    
    if guess == secret:
        print("恭喜你猜对了！")
        guessed = True
    elif guess > secret:
        print("猜大了，再小一点！")
    else:
        print("猜小了，再大一点！")

print("游戏结束！")