# 倒计时火箭：从 N 倒数到 1，然后发射
start = int(input("从几开始倒数？ "))
for n in range(start, 0, -1):
    print(n)
print("发射！🚀")
