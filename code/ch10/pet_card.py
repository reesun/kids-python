# 宠物档案卡：用字典记录宠物信息，练习增、删、改、查
pet = {"名字": "豆豆", "种类": "小狗", "年龄": 2}

# 查
print("名字：" + pet["名字"])

# 增
pet["爱吃"] = input("豆豆爱吃什么？ ")

# 改
pet["年龄"] = pet["年龄"] + 1
print("过生日啦，现在 " + str(pet["年龄"]) + " 岁")

# 删
del pet["种类"]

print("=== 宠物档案卡 ===")
for key in pet:
    print(key + "：" + str(pet[key]))
