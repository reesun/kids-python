# 猜拳裁判：输入两个人出的拳，判断谁赢
player_one = input("一号出什么（石头/剪刀/布）？ ")
player_two = input("二号出什么（石头/剪刀/布）？ ")
if player_one == player_two:
    print("平局！")
elif (player_one == "石头" and player_two == "剪刀") or \
     (player_one == "剪刀" and player_two == "布") or \
     (player_one == "布" and player_two == "石头"):
    print("一号赢！")
else:
    print("二号赢！")
