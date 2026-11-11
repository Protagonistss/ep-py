"""作业 2:乘法口诀生成器

输入一个数字 n,打印 n 的乘法口诀:1×n 到 9×n。

运行:uv run python exercises/02_flow/homework_times_table.py
预期效果:
    想看几的口诀? 7
    1 x 7 = 7
    2 x 7 = 14
    ...(一直到这里)
    9 x 7 = 63
"""

# TODO: 用 input() 读取数字 n,并转成 int
# TODO: 用 for + range(1, 10) 让 i 从 1 数到 9(注意:range 含头不含尾)
# TODO: 每圈用 f-string 打印一行:{i} x {n} = 两个数相乘的结果
# 挑战:用两层 for 嵌套,打印完整九九乘法表(1x1=1 到 9x9=81)
