#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/8/21 09:20
# @Author  : Lynn
# @Site    : 
# @File    : np_test.py
# @Software: PyCharm

import numpy as np
import time
import schedule


def main():
    import schedule
    import time

    def job():
        print("I'm working...")

    schedule.every(10).minutes.do(job)
    schedule.every().hour.do(job)
    schedule.every().day.at("10:30").do(job)
    schedule.every(5).to(10).days.do(job)
    schedule.every().monday.do(job)
    schedule.every().wednesday.at("13:15").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
    # import time
    #
    # begin_time = time.perf_counter()  # 这里使用time.time()也可以，避免使用time.clock()
    # print(begin_time)
    # time.sleep(5)
    # time_elapsed = time.perf_counter() - begin_time
    # print(time_elapsed)

    # for i in range(1, 4):  # 外层循环
    #     print('第%s次循环。' % i)
    #
    #     for n in range(1, 4):  # 内层循环
    #         if n == i:
    #             print('遇见数%s。' % n)
    #             break
    #         print('%s' % n, end=',')
    #
    #     print('已跳出第%s次内层循环。' % i)


if __name__ == '__main__':
    main()
