# 小卖部计算器：输入单价和数量，算出应付金额
item_name = input("买什么？ ")
price = float(input("单价是多少元？ "))
count = int(input("买几个？ "))
total = price * count
print(item_name + " 一共 " + str(count) + " 个")
print("应付：" + str(round(total, 2)) + " 元")
