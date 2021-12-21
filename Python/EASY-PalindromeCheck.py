class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        l = []
        for i in s:
            if (i >= 'a' and i <= 'z') or (i >= '0' and i <= '9'):
                l.append(i)

        if l == list(reversed(l)):
            return True
        return False


# https://leetcode.com/problems/palindrome-linked-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = []
        while head != None:
            l.append(head.val)
            head = head.next

        return l == list(reversed(l))