import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gbk')

name = input('请输入你的名字：')
year = input('请输入你的出生年份：')
age = 2026 - int(year)
print(name + '，你今年' + str(age) + '岁啦！')