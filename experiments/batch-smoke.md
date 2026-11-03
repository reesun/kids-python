# 全书批测记录

实测时间：2026-11-03 16:53（UTC+8，北京时间）。环境：Python 3.13.5，工作目录为书稿根目录 `/workspace/books/kids-python/`。

交互脚本一律用 `printf` 喂入。第 14 章在脚本外先固定随机种子 42，这样答案每次都是 82，脚本本身没有改动。第 13 章用 turtle 画图，实测机没有装 tkinter，所以只做编译检查，记为未测，需要在有窗口的电脑上再跑一次。第 12 章的 buggy.py 本来就是故意写错的，报 TypeError 才算符合预期。

## ch03 · hello_dressup.py

```bash
printf '小明\n' | python3 code/ch03/hello_dressup.py
```

退出码：0。结果：通过。

```text
你叫什么名字？ 你好，小明！
今天我们用 Python 跟电脑说话。
```

## ch04 · intro_generator.py

```bash
printf '小明\n画画\n' | python3 code/ch04/intro_generator.py
```

退出码：0。结果：通过。

```text
你叫什么名字？ 你最喜欢做什么？ 大家好，我叫小明。
我最喜欢画画，很高兴认识你们！
```

## ch05 · shop_calculator.py

```bash
printf '铅笔\n1.5\n4\n' | python3 code/ch05/shop_calculator.py
```

退出码：0。结果：通过。

```text
买什么？ 单价是多少元？ 买几个？ 铅笔 一共 4 个
应付：6.0 元
```

## ch06 · rps_judge.py（一号赢）

```bash
printf '石头\n剪刀\n' | python3 code/ch06/rps_judge.py
```

退出码：0。结果：通过。

```text
一号出什么（石头/剪刀/布）？ 二号出什么（石头/剪刀/布）？ 一号赢！
```

## ch06 · rps_judge.py（平局）

```bash
printf '布\n布\n' | python3 code/ch06/rps_judge.py
```

退出码：0。结果：通过。

```text
一号出什么（石头/剪刀/布）？ 二号出什么（石头/剪刀/布）？ 平局！
```

## ch06 · rps_judge.py（二号赢）

```bash
printf '剪刀\n石头\n' | python3 code/ch06/rps_judge.py
```

退出码：0。结果：通过。

```text
一号出什么（石头/剪刀/布）？ 二号出什么（石头/剪刀/布）？ 二号赢！
```

## ch07 · rocket_countdown.py

```bash
printf '5\n' | python3 code/ch07/rocket_countdown.py
```

退出码：0。结果：通过。

```text
从几开始倒数？ 5
4
3
2
1
发射！🚀
```

## ch08 · roll_call.py

```bash
python3 code/ch08/roll_call.py
```

退出码：0。结果：通过。

```text
开始点名，共 4 人
小明：到！
小红：到！
小刚：到！
小美：到！
点名结束！
```

## ch09 · mood_weather.py（开心）

```bash
printf '小明\n开心\n' | python3 code/ch09/mood_weather.py
```

退出码：0。结果：通过。

```text
你叫什么名字？ 今天心情怎么样（开心/难过/生气/其他）？ 📺 心情天气播报：小明 今天是 晴天 ☀️
```

## ch09 · mood_weather.py（生气）

```bash
printf '小红\n生气\n' | python3 code/ch09/mood_weather.py
```

退出码：0。结果：通过。

```text
你叫什么名字？ 今天心情怎么样（开心/难过/生气/其他）？ 📺 心情天气播报：小红 今天是 打雷 ⛈️
```

## ch10 · pet_card.py

```bash
printf '骨头\n' | python3 code/ch10/pet_card.py
```

退出码：0。结果：通过。

```text
名字：豆豆
豆豆爱吃什么？ 过生日啦，现在 3 岁
=== 宠物档案卡 ===
名字：豆豆
年龄：3
爱吃：骨头
```

## ch11 · diary.py（第一次）

```bash
printf '今天学了函数\n' | python3 code/ch11/diary.py
```

退出码：0。结果：通过。

```text
今天想记什么？ === 我的日记 ===
· 今天学了函数
```

## ch11 · diary.py（第二次，追加）

```bash
printf '明天学字典\n' | python3 code/ch11/diary.py
```

退出码：0。结果：通过。

```text
今天想记什么？ === 我的日记 ===
· 今天学了函数
· 明天学字典
```

## ch12 · buggy.py（故意报错）

```bash
printf '9\n' | python3 code/ch12/buggy.py
```

退出码：1。结果：通过（按预期报错）。

```text
你几岁？ Traceback (most recent call last):
  File "/workspace/books/kids-python/code/ch12/buggy.py", line 3, in <module>
    next_year = age + 1
                ~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

## ch12 · fixed.py

```bash
printf '9\n' | python3 code/ch12/fixed.py
```

退出码：0。结果：通过。

```text
你几岁？ 明年你就 10 岁啦！
```

## ch14 · guess_number.py（种子 42，猜中）

```bash
printf '50\n75\n88\n81\n84\n82\n' | python3 -c "import random; random.seed(42); exec(open('code/ch14/guess_number.py', encoding='utf-8').read())"
```

退出码：0。结果：通过。

```text
我想好了一个 1～100 的数字，你有 7 次机会！
第 1 次，你猜是几？ 小了！
第 2 次，你猜是几？ 小了！
第 3 次，你猜是几？ 大了！
第 4 次，你猜是几？ 小了！
第 5 次，你猜是几？ 大了！
第 6 次，你猜是几？ 猜对了！你用了 6 次。
```

## ch14 · guess_number.py（种子 42，七次用完）

```bash
printf '1\n2\n3\n4\n5\n6\n7\n' | python3 -c "import random; random.seed(42); exec(open('code/ch14/guess_number.py', encoding='utf-8').read())"
```

退出码：0。结果：通过。

```text
我想好了一个 1～100 的数字，你有 7 次机会！
第 1 次，你猜是几？ 小了！
第 2 次，你猜是几？ 小了！
第 3 次，你猜是几？ 小了！
第 4 次，你猜是几？ 小了！
第 5 次，你猜是几？ 小了！
第 6 次，你猜是几？ 小了！
第 7 次，你猜是几？ 小了！
机会用完啦，答案是 82。
```

## ch15 · height_chart.py

```bash
python3 code/ch15/height_chart.py
```

退出码：0。结果：通过。

```text
=== 班级身高统计 ===
人数：5
平均身高：132.4 厘米
最高：小刚 141 厘米
最矮：小美 125 厘米

=== 身高柱状图（每个■代表 5 厘米） ===
小明 | ■■■■■■■■■■■■■■■■■■■■■■■■■■ 132
小红 | ■■■■■■■■■■■■■■■■■■■■■■■■■ 128
小刚 | ■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 141
小美 | ■■■■■■■■■■■■■■■■■■■■■■■■■ 125
小李 | ■■■■■■■■■■■■■■■■■■■■■■■■■■■ 136
```

## ch16 · mini_shop.py

```bash
printf '铅笔\n4\n橡皮\n1\n糖果\n2\n\n' | python3 code/ch16/mini_shop.py
```

退出码：0。结果：通过。

```text
=== 今日商品 ===
铅笔：1.5 元
橡皮：2 元
笔记本：5 元
贴纸：3 元
买什么？（直接回车结账） 买几个？ 已加入：铅笔 × 4
买什么？（直接回车结账） 买几个？ 已加入：橡皮 × 1
买什么？（直接回车结账） 买几个？ 没有这个商品：糖果
买什么？（直接回车结账） === 小票 ===
铅笔 × 4 = 6.0 元
橡皮 × 1 = 2 元
合计：8.0 元
```

## ch13 · maze.py（只编译）

```bash
python3 -m py_compile code/ch13/maze.py && echo COMPILE_OK
```

退出码：0。结果：未测（只编译通过）。

```text
COMPILE_OK
```

运行后生成的 `code/ch16/receipt.txt` 内容如下，和屏幕上的小票一致：

```text
铅笔 × 4 = 6.0 元
橡皮 × 1 = 2 元
合计：8.0 元
```

运行后生成的 `code/ch11/diary.txt` 内容如下，第二次运行是追加写入：

```text
今天学了函数
明天学字典
```

## 汇总

| 章 | 脚本 | 退出码 | 结果 |
| --- | --- | --- | --- |
| ch03 | hello_dressup.py | 0 | 通过 |
| ch04 | intro_generator.py | 0 | 通过 |
| ch05 | shop_calculator.py | 0 | 通过 |
| ch06 | rps_judge.py（一号赢） | 0 | 通过 |
| ch06 | rps_judge.py（平局） | 0 | 通过 |
| ch06 | rps_judge.py（二号赢） | 0 | 通过 |
| ch07 | rocket_countdown.py | 0 | 通过 |
| ch08 | roll_call.py | 0 | 通过 |
| ch09 | mood_weather.py（开心） | 0 | 通过 |
| ch09 | mood_weather.py（生气） | 0 | 通过 |
| ch10 | pet_card.py | 0 | 通过 |
| ch11 | diary.py（第一次） | 0 | 通过 |
| ch11 | diary.py（第二次，追加） | 0 | 通过 |
| ch12 | buggy.py（故意报错） | 1 | 通过（按预期报错） |
| ch12 | fixed.py | 0 | 通过 |
| ch14 | guess_number.py（种子 42，猜中） | 0 | 通过 |
| ch14 | guess_number.py（种子 42，七次用完） | 0 | 通过 |
| ch15 | height_chart.py | 0 | 通过 |
| ch16 | mini_shop.py | 0 | 通过 |
| ch13 | maze.py（只编译） | 0 | 未测（只编译通过） |

说明：`input` 的提示语末尾没有换行，所以用管道喂入时，提示和下一行输出会挤在同一行，这是正常现象。

顺手发现两处小问题，都没有改脚本，留给作者决定。第一处，第 5 章和第 16 章的金额会出现「6.0 元」和「2 元」混排，因为单价有小数时结果是浮点数。第二处，第 16 章输入不存在的商品（如「糖果」）时，脚本先问「买几个」再提示没有这个商品，顺序可以调整成先判断商品再问数量。

测完已删除运行产物：`code/ch11/diary.txt`、`code/ch16/receipt.txt` 和所有 `__pycache__` 目录。
