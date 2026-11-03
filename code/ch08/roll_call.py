# 班级点名册：用列表存名字，挨个点名
students = ["小明", "小红", "小刚", "小美"]
print("开始点名，共 " + str(len(students)) + " 人")
for student in students:
    print(student + "：到！")
print("点名结束！")
