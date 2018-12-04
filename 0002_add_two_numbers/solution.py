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

class Solution1:
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
        if num > 10:
            current.next = self.numToListNode(num // 10)

        return current 

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
result = ListNode(7)
result.next = ListNode(0)
result.next.next = ListNode(8)

def test_list_node_to_num_1():
    assert Solution1().listNodeToNum(l1) == 342

def test_list_node_to_num_2():
    assert Solution1().listNodeToNum(l2) == 465

def test_num_to_list_node():
    assert list(Solution1().numToListNode(807)) == list(result)

def test_add_two_numbers():
    assert list(Solution1().addTwoNumbers(l1, l2)) == list(result)

