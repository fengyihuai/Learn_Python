# -*- coding:UTF-8 -*-

import time

timestamp = 1566961974.0
# 利用Localtime()函数将时间戳转化成时间数组
localtime = time.localtime(timestamp)
print(localtime)    # time.struct_time(tm_year=2019, tm_mon=8, tm_mday=28, tm_hour=11, tm_min=12, tm_sec=54, tm_wday=2, tm_yday=240, tm_isdst=0)
# structtime: https://stackoverflow.com/questions/9551514/structseq-error-with-time-struct-time
time.struct_time((2019, 8, 28, 11, 12, 54, 2, 240, 0))
# 利用strfttime()函数重新格式化时间
dt = time.strftime("%Y:%m:%d %H:%M:%S", localtime)
print(dt)   # 2019:08:28 11:12:54