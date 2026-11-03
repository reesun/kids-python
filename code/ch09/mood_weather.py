# 心情天气播报：用自己定义的函数，把心情变成天气
def mood_to_weather(mood):
    if mood == "开心":
        return "晴天 ☀️"
    elif mood == "难过":
        return "小雨 🌧️"
    elif mood == "生气":
        return "打雷 ⛈️"
    else:
        return "多云 ☁️"


def broadcast(name, mood):
    weather = mood_to_weather(mood)
    print("📺 心情天气播报：" + name + " 今天是 " + weather)


name = input("你叫什么名字？ ")
mood = input("今天心情怎么样（开心/难过/生气/其他）？ ")
broadcast(name, mood)
