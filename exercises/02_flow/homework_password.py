"""作业 3:密码锁

预设密码存在下面的变量里,用户最多输入 3 次:
对了就开锁,3 次都错就锁死。

运行:uv run python exercises/02_flow/homework_password.py
预期效果:
    请输入密码: 123
    密码错误,还剩 2 次机会
    请输入密码: 321
    密码错误,还剩 1 次机会
    请输入密码: 000
    已锁死,请 100 年后再试
"""

PASSWORD = "py2024"   # 变量名全大写 = "这个值定好了不再改"的约定写法

# TODO: 建两个变量:chances = 3(剩余机会)、opened = False(是否开锁成功)
# TODO: 用 while 循环:只要 chances > 0 就继续问
# TODO: 循环里 input 读密码:
#   - 猜对了:打印"🔓 开锁成功",opened = True,然后 break
#   - 猜错了:chances 减 1;只要还有机会,就提示"密码错误,还剩 x 次机会"
# TODO: 循环结束后,if not opened:打印"已锁死,请 100 年后再试"
#   (opened 就是第 2 课概念卡里的 bool——用 True/False 记录"事情发生没发生")
