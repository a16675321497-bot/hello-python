import json

# 函数1：从文件读取通讯录
def load_contacts():
    try:
        with open("contacts.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

# 函数2：保存通讯录到文件
def save_contacts(contacts):
    with open("contacts.json", "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)

# 函数3：添加联系人
def add_contact(contacts):
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    contacts[name] = phone
    save_contacts(contacts)
    print("添加成功！")

# 函数4：查看所有联系人
def show_all(contacts):
    if len(contacts) == 0:
        print("通讯录是空的！")
    else:
        print("=== 通讯录 ===")
        for name, phone in contacts.items():
            print(name + "：" + phone)

# 函数5：查找联系人
def find_contact(contacts):
    name = input("请输入要查找的姓名：")
    if name in contacts:
        print(name + "的电话：" + contacts[name])
    else:
        print("找不到这个人！")

# 主程序
contacts = load_contacts()

while True:
    print("\n=== 通讯录菜单 ===")
    print("1. 添加联系人")
    print("2. 查看所有联系人")
    print("3. 查找联系人")
    print("4. 退出")

    choice = input("请选择（1-4）：")

    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        show_all(contacts)
    elif choice == "3":
        find_contact(contacts)
    elif choice == "4":
        print("再见！")
        break
    else:
        print("输入错误，请重新选择！")