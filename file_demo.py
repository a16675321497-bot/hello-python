# 写文件：把内容写到test.txt里
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("你好，这是我的第一个文件！\n")
    f.write("第二行内容\n")
    f.write("第三行内容\n")

print("文件写入成功！")

# 读文件：从test.txt里读内容
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("文件内容：")
    print(content)
