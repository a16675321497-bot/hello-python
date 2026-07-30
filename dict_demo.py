# 创建一个字典
person = {"名字": "潘江波", "年龄": 33, "职业": "外卖员"}

# 打印整个字典
print("字典内容：", person)

# 取某个值
print("名字是：", person["名字"])
print("年龄是：", person["年龄"])

# 修改某个值
person["年龄"] = 34
print("修改后年龄：", person["年龄"])

# 添加新的键值对
person["城市"] = "北京"
print("添加后：", person)

# 删除一个键值对
del person["职业"]
print("删除后：", person)

# 看看字典有几个键值对
print("一共有", len(person), "个键值对")
