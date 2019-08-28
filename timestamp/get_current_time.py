# -*- coding:UTF-8 -*-

import time

# 获取当前时间
current_time = int(time.time())
print(current_time) # 1566966308
# 转换为localtime
localtime = time.localtime(current_time)
# 利用strftime()函数重新格式化时间
dt = time.strftime("%Y:%m:%d %H:%M:%S", localtime)
print(dt)   # 返回当前时间：2019:08:28 12:25:08