# 创建一个列表
fruits = ["苹果", "香蕉", "西瓜", "葡萄"]

# 打印整个列表
print("列表内容：", fruits)

# 打印第1个（编号0）
print("第1个水果：", fruits[0])

# 打印最后一个
print("最后一个水果：", fruits[-1])

# 修改列表里的值
fruits[1] = "草莓"
print("修改后：", fruits)

# 添加新水果
fruits.append("芒果")
print("添加后：", fruits)

# 删除一个水果
fruits.remove("苹果")
print("删除后：", fruits)

# 看看列表有几个水果
print("一共有", len(fruits), "个水果")