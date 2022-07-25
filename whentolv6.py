# 版权 / copyright
"""
Power by meterax
Version:1.0
E-mail:meterax@outlook.com
QQ:3288974043
"""


# 主程序 / main program
print("语言 / Language\n1.ZH-CN\n2.English")
language = input("enter 1-2:")
language = int(language)
if language == 1:
    print("何时到lv6")
    print("Power by meterax")
    now_lv_str = input("请输入你的经验值:")
    now_bb_str = input("请输入当前币:")
elif language == 2:
    print("When to lv6")
    print("Power by meterax")
    now_lv_str = input("Enter your lv:")
    now_bb_str = input("Enter your B-coin:")

# 算法 / algorithm
now_lv = int(now_lv_str)
now_bb = int(now_bb_str)
need_lv = 28800 - now_lv
need_lv_day = need_lv / 60
now_bb_lv = now_bb * 10
get_bb_lv_day = now_bb_lv / 50
need_day = need_lv_day - get_bb_lv_day
if need_day < 0:
    need_day = 0
elif need_day > int(need_day):
    need_day = int(need_day) + 1

# 结果 / result
if language == 1:
    print("还需要", need_day, "天")
elif language == 2:
    print("Only need", need_day, "day")
