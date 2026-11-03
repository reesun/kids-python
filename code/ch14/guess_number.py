# 猜数字加强版：1～100 之间，最多猜 7 次，每次提示大了还是小了
import random

secret = random.randint(1, 100)
max_tries = 7
tries = 0
won = False

print("我想好了一个 1～100 的数字，你有 " + str(max_tries) + " 次机会！")
while tries < max_tries:
    guess = int(input("第 " + str(tries + 1) + " 次，你猜是几？ "))
    tries = tries + 1
    if guess > secret:
        print("大了！")
    elif guess < secret:
        print("小了！")
    else:
        print("猜对了！你用了 " + str(tries) + " 次。")
        won = True
        break

if not won:
    print("机会用完啦，答案是 " + str(secret) + "。")
