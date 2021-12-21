package com.company;

/**
 * https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem
 */
class NodeX {
    int data;
    NodeX next;
}
public class LinkedListHasCycle {

    boolean hasCycle(NodeX head) {
        if (head == null) return false;
        if (head.next == null) return false;

        NodeX fast = head.next.next;
        NodeX slow = head;
        while (fast != null)
        {
            if (fast == slow)
            {
                return true;
            }
            slow = slow.next;
            fast = fast.next;
            if (fast == null) return false;
            else fast = fast.next;

        }

        return false;
    }
}
