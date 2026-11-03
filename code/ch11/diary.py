# 日记本：把今天的话追加写进 diary.txt，再全部读出来
from pathlib import Path

diary_path = Path(__file__).parent / "diary.txt"

entry = input("今天想记什么？ ")
with open(diary_path, "a", encoding="utf-8") as diary_file:
    diary_file.write(entry + "\n")

print("=== 我的日记 ===")
with open(diary_path, "r", encoding="utf-8") as diary_file:
    for line in diary_file:
        print("· " + line.strip())
