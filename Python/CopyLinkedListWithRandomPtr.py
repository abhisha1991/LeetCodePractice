# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# https://discuss.leetcode.com/topic/18086/java-o-n-solution/2
# CLEVER SOLUTION!! USING A HASHMAP
# here in c# https://paste.ofcode.org/4LiWNQqWDybrk2FaPH5ahL
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = dict()
        node = head

        if head is None:
            return None

        # build a dictionary with only the label values,
        # no value in the dictionary is associated to any other value in the dictionary right now
        while node is not None:
            dic[node] = RandomListNode(node.label)
            node = node.next

        node = head
        # assign the next and random pointers now for the new fragmented values in the dictionary
        # so that now they can be connected to each other
        while node is not None:
            dic[node].next = node.next
            dic[node].random = node.random
            node = node.next

        return dic[head]


s = Solution()
h = RandomListNode(1)
print("Address of h is", h)
h.next = RandomListNode(2)
print("Address of h is", h.next)
h.next.next = RandomListNode(3)
print("Address of h is", h.next.next)
h.next.random = h.next

x = s.copyRandomList(h)
print("Got the solution")
while x is not None:
    print(x.label)
    print("Address of x is", x)
    print("Moving to next node")
    x = x.next
