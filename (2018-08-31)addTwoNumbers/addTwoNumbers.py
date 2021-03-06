#!/usr/bin/env python
# coding: utf-8

# https://leetcode.com/problems/add-two-numbers/description/
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # for でまとめるために lis にしています。
        lis = [0, 0]
        for i,l in enumerate([l1, l2]):

            # ListNode ってのがよくわからないんだけど´´
            # while と l=l.next でイテレ�`トできるらしいからそれに惄い泙后�
            _ = ''
            while l:
                _ += str(l.val)
                l = l.next
            lis[i] = int(''.join(reversed(list(_))))

        # ListNode の碧��參翌は�eに���g´´。
        added = sum(lis)
        return list(map(lambda l:int(l), reversed(list(str(added)))))
