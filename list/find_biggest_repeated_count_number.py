#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 11:15 下午
# @Author  : yang_cube
# @Site    : 
# @File    : find_biggest_repeated_count_number.py
# @Software: PyCharm


class BiggestRepeatedCountNumber:
    arrList = [10, 3, 4, 5, 72, 8, 5, 2, 1, 3, 5, 2, 6, 8, 1, 2, 3, 5]

    # 普通做法
    def general(self):

        all_dict = {}
        for i in self.arrList:
            buffer = all_dict.get(i)
            if buffer is None:
                buffer = []
            buffer.append(i)
            all_dict[i] = buffer

        count = 0
        for key, value in all_dict.items():
            if len(value) > count:
                count = len(value)
                number = key

        print("=== Print from general: ===")
        print(all_dict)
        print("number: {}, count {}".format(number, count))

    # 进阶做法
    def advance(self):
        count = 0
        number = None
        for i in self.arrList:
            if self.arrList.count(i) > count:
                count = self.arrList.count(i)
                number = i
        print("=== Print from advance: ===")
        print("number: {}, count {}".format(number, count))


calculator = BiggestRepeatedCountNumber()
calculator.general()
calculator.advance()
