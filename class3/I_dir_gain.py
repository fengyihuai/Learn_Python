# -*- coding: UTF-8 -*-
# 1、输出当前文件所在的目录；

import os
import sys

# strategy A
if __name__ == "__main__": # 希望返回主函数路径
    print(os.path.realpath(sys.argv[0]))
    print(os.path.split(os.path.realpath(sys.argv[0])))
    print(os.path.split(os.path.realpath(sys.argv[0]))[0])
    # print(os.path.split(os.path.realpath(sys.argv[0]))[1])
# strategy B
print('the current file ',
      os.path.basename(__file__),
      'is in:')
print(os.getcwd())
print(__file__)

print()