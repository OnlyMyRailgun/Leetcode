# -*- coding: utf-8 -*-

class Solution:
    def find_two_sum(self, array, target):
        index_by_value = {}
        for index, value in enumerate(array):
            target_index = index_by_value.get(target - value)
            if target_index != None:
                return [target_index, index]
            index_by_value[value] = index

def test_return_0_1():
    assert Solution().find_two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_return_1_2():
    assert Solution().find_two_sum([2, 7, 11, 15], 18) == [1, 2]

def test_return_0_2():
    assert Solution().find_two_sum([3, 7, 3], 6) == [0, 2]

