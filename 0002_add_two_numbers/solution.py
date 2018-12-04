# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

    def __iter__(self):
        current = self
        while current != None:
            yield current.val
            current = current.next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.numToListNode(
            self.listNodeToNum(l1) + self.listNodeToNum(l2)
        )
        
    def listNodeToNum(self, ls):
        """
        :type ls: ListNode
        :rtype: int
        """
        if ls.next:
            return ls.val + self.listNodeToNum(ls.next) * 10
        else:
            return ls.val

    def numToListNode(self, num):
        """
        :type num: int
        :rtype: ListNode
        """
        current = ListNode(num % 10)
        if num > 9:
            current.next = self.numToListNode(num // 10)

        return current 

def arrayToListNode(array):
    """
    :type array: int[]
    :rtype ListNode:
    """
    if len(array) == 0:
        raise Exception('empty array!')
    elif len(array) == 1:
        return ListNode(array[0])
    else:
        current = ListNode(array.pop(0))
        current.next = arrayToListNode(array)
        return current

def test_list_node_to_num_1():
    ls = arrayToListNode([2, 4, 3])
    assert Solution().listNodeToNum(ls) == 342

def test_list_node_to_num_2():
    ls = arrayToListNode([5, 6, 4])
    assert Solution().listNodeToNum(ls) == 465

def test_num_to_list_node():
    assert list(Solution().numToListNode(807)) == [7, 0, 8] 

def test_add_two_numbers():
    assert list(Solution().addTwoNumbers(
        arrayToListNode([2, 4, 3]),
        arrayToListNode([5, 6, 4])
    )) == [7, 0, 8]

def test_list_node_to_num3():
    ls = arrayToListNode([1])
    assert Solution().listNodeToNum(ls) == 1

def test_list_node_to_num4():
    ls = arrayToListNode([9, 9])
    assert Solution().listNodeToNum(ls) == 99

def test_num_to_list_node_2():
    assert list(Solution().numToListNode(100)) == [0, 0, 1]

def test_add_two_numbers_2():
    list1 = arrayToListNode([1])
    list2 = arrayToListNode([9, 9])
    rslt = arrayToListNode([0, 0, 1])
    assert list(Solution().addTwoNumbers(list1, list2)) == list(rslt)

