# BMI计算器
身高 = float(input("请输入你的身高（米）："))
体重 = float(input("请输入你的体重（公斤）："))

bmi = 体重 / (身高 * 身高)
bmi = round(bmi, 1)

print("你的BMI是：", bmi)

if bmi < 18.5:
    print("偏瘦")
elif bmi < 24:
    print("正常")
elif bmi < 28:
    print("偏胖")
else:
    print("肥胖")