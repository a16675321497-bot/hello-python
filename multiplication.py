# 外层循环：1到9
for i in range(1, 10):
    # 内层循环：1到i
    for j in range(1, i + 1):
        # 打印乘法公式，不换行
        print(f"{j} x {i} = {i*j}", end="\t")
    # 每行结束后换行
    print()