class LinkedList(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_single_ll(head):
    curr = head
    prev = None
    next = curr.next
    while curr is not None:

        curr.next = prev
        prev = curr
        curr = next
        if curr is None:
            break
        next = curr.next

    return prev


def create_ll(curr, val):
    ll = LinkedList(val)
    curr.next = ll


head = LinkedList(1)
i = 2
curr = head
while i < 100:
    create_ll(curr, i)
    i += 1
    curr = curr.next


head = reverse_single_ll(head)
while head is not None:
    print(head.val)
    head = head.next
