class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# try going through an example of  l1 = 1-->3-->5-->7 and l2 = 2-->4-->6,
# the task is to merge these 2
'''
The idea is to create a temp node x = 0
and point p to it
p = x
where x.val = some value, say 0
and x.next = None

Compare l1 and l2's val, if l1.val < l2.val, means that p should point to l1
p = x => p.next = l1
0 --> 1 --> 3 --> 5 --> 7
p
Now l1 = l1.next makes l1 point to 3, p = p.next makes p point to 1
0 --> 1 --> 3 --> 5 --> 7
x     p     l1
Now l2.val < l1.val
so p.next = l2, we have 
0 --> 1 --> 2 --> 4 --> 6
x     p     l2
l2 = l2.next and p = p.next
0 --> 1 --> 2 --> 4 --> 6
x           p     l2
So basically we have 3 things till now l1 = 3 --> 5 --> 7, l2 = 4 --> 6
and x to p, which is 0 --> 1 --> 2
at the end, we return x.next, which is the head of the list
'''
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        x = head  # slow
        y = head  # fast
        # prev is used to mark end of first list
        prev = None
        while y != None and y.next != None:
            prev = x
            x = x.next
            y = y.next.next

        # prev is one behind x = x is starting of the right list, meaning prev must be end of first list
        prev.next = None

        l1 = self.sortList(head)  # head is start of first list, prev is end of first list
        l2 = self.sortList(x)  # x is start of second list

        return self.merge(l1, l2)

    def merge(self, l1, l2):
        x = ListNode(0)
        p = x
        while (l1 != None and l2 != None):
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        while l1 != None:
            p.next = l1
            l1 = l1.next
            p = p.next

        while l2 != None:
            p.next = l2
            l2 = l2.next
            p = p.next

        return x.next



