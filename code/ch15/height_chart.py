# 班级身高统计图：用列表和字典算平均、最高、最矮，再画文字柱状图
heights = {"小明": 132, "小红": 128, "小刚": 141, "小美": 125, "小李": 136}

total = 0
for name in heights:
    total = total + heights[name]
average = total / len(heights)

tallest = max(heights, key=heights.get)
shortest = min(heights, key=heights.get)

print("=== 班级身高统计 ===")
print("人数：" + str(len(heights)))
print("平均身高：" + str(round(average, 1)) + " 厘米")
print("最高：" + tallest + " " + str(heights[tallest]) + " 厘米")
print("最矮：" + shortest + " " + str(heights[shortest]) + " 厘米")
print()
print("=== 身高柱状图（每个■代表 5 厘米） ===")
for name in heights:
    bar = "■" * (heights[name] // 5)
    print(name + " | " + bar + " " + str(heights[name]))
