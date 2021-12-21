# Definition for singly-linked list.
# https://leetcode.com/problems/add-two-numbers/description/


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        i = l1
        count1 = 0
        while i != None:
            count1 += 1
            i = i.next

        j = l2
        count2 = 0
        while j != None:
            count2 += 1
            j = j.next

        i = l1
        j = l2
        # Take the longer list as the primary one where you will be storing all sums
        if count1 > count2:
            # make l1 as primary
            while j != None:
                i.val = i.val + j.val
                i = i.next
                j = j.next
        else:
            # make l2 as primary
            while i != None:
                j.val = j.val + i.val
                i = i.next
                j = j.next

        k = 0
        # set the carry over list. Remember, YOU NEED TO SET COUNT + 1 ZEROS! - why?
        # leading 5 -> 6 -> 7 and 5 -> 6 -> 7 gives 0 -> 3 -> 5 -> 1 [New node added at end]
        if count1 > count2:
            carry = [0] * (count1 + 1)
            res = l1
        else:
            carry = [0] * (count2 + 1)
            res = l2

        while res != None:
            prev = res
            res.val += carry[k]
            # carry overs
            if res.val > 9:
                # carry for the next set of number is to be set to 1
                carry[k + 1] = 1
                res.val -= 10
            k += 1
            res = res.next

        if carry[k] == 1:
            # if we did get a spill over from the last addition
            # create new node with carry over 1
            prev.next = ListNode(1)

        # return primary list
        if count1 > count2:
            return l1
        return l2
