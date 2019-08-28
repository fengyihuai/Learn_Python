# -*- coding:UTF-8 -*-
import time

dt = "2019-08-28 11:12:54"

# 将时间转换成时间数组
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
# 转换成时间戳
print(timeArray)    # time.struct_time(tm_year=2019, tm_mon=8, tm_day=28, tm_hour=11, tm_min=12, tm_sec=54, tm_wday=2, tm_yday=220, tm_isdst=-1)
print(timeArray[0])    # 2019
# 讲时间数组转换成时间戳
timestamp = time.mktime(timeArray)
print(timestamp)    # 1566961974.0