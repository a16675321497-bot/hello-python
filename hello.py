import sys
import locale
# 设置系统编码为终端支持的编码
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

name = input('请输入你的名字：')
year = input('请输入你的出生年份：')
age = 2026 - int(year)
print(name + '，你今年' + str(age) + '岁啦！')