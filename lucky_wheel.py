import random
import time

# 参与抽奖的名单
名单 = ["小明", "小红", "小刚", "小丽", "阿强", "阿花", "老王", "小李"]

print("=== 抽奖转盘开始！===")
print("参与人员：", 名单)

input("按回车键开始抽奖...")

# 模拟转盘转动效果
print("\n转盘转动中...")
for i in range(10):
    print("\r中奖者是：" + random.choice(名单), end="")
    time.sleep(0.1)

# 最终结果
中奖者 = random.choice(名单)
print("\n\n🎉 恭喜 " + 中奖者 + " 中奖了！🎉")