"""课堂项目:猜数字游戏

电脑随机想一个 1~100 的整数,你来猜。它只提示"大了 / 小了",
直到猜中为止,最后告诉你一共用了几次。

运行:uv run python exercises/02_flow/guess_number.py
讲义:lessons/02_guess_number.md 环节 ⑥
"""

import random

# 步骤 1:让电脑随机出题:answer = random.randint(1, 100)
#   (调试小技巧:第一版可以先写死 answer = 50,跑通后再换随机)

# 步骤 2:建计数器 count = 0,用来记录猜了几次

# 步骤 3:用 while True 开循环,循环里:
#   - input 读取你猜的数字,记得 int() 转成整数(第 1 课的坑,别再踩)
#   - 每猜一次,count 加 1

# 步骤 4:用 if / elif / else 判断并提示:
#   - 猜大了 → 打印"猜大了!"
#   - 猜小了 → 打印"猜小了!"
#   - 猜对了 → 打印恭喜 + 一共用了几次,然后 break 跳出循环

# 步骤 5(挑战):限制最多 7 次机会,每次提示还剩几次,用完判负
