# -*- coding:UTF-8 -*-

import time

dt = "2019-08-28 11:12:54"
# 利用strptime()函数将时间转换成时间数组
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
# 利用strftime()函数重新格式化时间
dt_new = time.strftime("%Y-%m-%d - %H:%M:%S", timeArray)
print(dt_new)   # 2019-08-28 - 11:12:54