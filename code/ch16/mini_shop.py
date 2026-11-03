# 综合大项目：简易商店——函数 + 字典 + 列表 + 循环 + 判断 + 文件
from pathlib import Path

goods = {"铅笔": 1.5, "橡皮": 2, "笔记本": 5, "贴纸": 3}
cart = []
receipt_path = Path(__file__).parent / "receipt.txt"


def show_goods():
    print("=== 今日商品 ===")
    for item in goods:
        print(item + "：" + str(goods[item]) + " 元")


def add_to_cart(item, count):
    if item in goods:
        cart.append([item, count])
        print("已加入：" + item + " × " + str(count))
    else:
        print("没有这个商品：" + item)


def checkout():
    total = 0
    lines = []
    for item, count in cart:
        cost = goods[item] * count
        total = total + cost
        lines.append(item + " × " + str(count) + " = " + str(cost) + " 元")
    lines.append("合计：" + str(total) + " 元")
    with open(receipt_path, "w", encoding="utf-8") as receipt_file:
        for line in lines:
            receipt_file.write(line + "\n")
    print("=== 小票 ===")
    for line in lines:
        print(line)


show_goods()
while True:
    item = input("买什么？（直接回车结账） ")
    if item == "":
        break
    count = int(input("买几个？ "))
    add_to_cart(item, count)
checkout()
