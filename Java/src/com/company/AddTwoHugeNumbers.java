package com.company;

import java.util.Collection;
import java.util.Iterator;
import java.util.List;
import java.util.ListIterator;
import java.util.ArrayList;
/**
 * Created by abhisha on 8/7/2017.
 */
class ListNode<T>
{
     ListNode(T x)
     {
        value = x;
     }

   T value;
   ListNode<T> next;
}

public class AddTwoHugeNumbers {

    public static ListNode<Integer> addTwoHugeNumbers(ListNode<Integer> a, ListNode<Integer> b)
    {
        final int max = 9999;
        final int maxDigitCount = 4;
        int lena = lenOfLinkedList(a);
        int lenb = lenOfLinkedList(b);
        int diff = lena - lenb;
        ListNode<Integer> result = new ListNode<>(0);
        // A is bigger than B, add diff number of nodes to 'B'
        if (diff > 0)
        {
            b = addNodesToLinkedList(b, diff,0);
        }
        else if (diff < 0)
        {
            a = addNodesToLinkedList(a, Math.abs(diff), 0);
        }
        ListNode<Integer> head = a;
        int len = lenOfLinkedList(a);
        for (int i = 0; i < len; i++)
        {
            int sum = a.value + b.value;

            // store the sum temporarily
            a.value = sum;
            a = a.next;
            b = b.next;
        }

        int count = 0;
        while (count < len - 1 && len >= 2)
        {
            ListNode<Integer> atemp, atempPrev;
            atemp = returnValueAt(head, len - 1 - count);
            atempPrev = returnValueAt(head, len - 2 - count);
            if (atemp.value > max)
            {
                atemp.value -= max + 1;
                atempPrev.value += 1;
            }
            count++;
        }

        a = head;
        if (a.value > max)
        {
            a.value -= max+1;
            head = addNodesToLinkedList(a, 1, 1);
        }

        return  head;
    }

    public static ListNode<Integer> returnValueAt(ListNode<Integer> x, int idx)
    {
        int count = 0;
        while (count < idx)
        {
            x = x.next;
            count++;
        }
        return x;
    }

    public static  ListNode<Integer> addNodesToLinkedList(ListNode<Integer> x, int nodeCount, int val)
    {
        // Add to beginning
        int count = 0;
        while (count < nodeCount)
        {
            ListNode<Integer> temp = new ListNode<>(val);
            temp.next = x;
            x = temp;
            count++;
        }
        return x;
    }

    public static int lenOfLinkedList(ListNode<Integer> x)
    {
        int count = 0;
        if (x == null) return 0;
        while (x != null)
        {
            count++;
            x = x.next;
        }
        return  count;
    }

    public static void addTwoHugeNumbersMain()
    {
        // a = 9876, 5432, 1999
        // b = 1, 8001
        ListNode<Integer> a = new ListNode(9876);
        a.next = new ListNode<>(5432);
        a.next.next = new ListNode<>(1999);

        ListNode<Integer> b = new ListNode<>(1);
        b.next = new ListNode<>(8001);

        addTwoHugeNumbers(a,b);
    }
}
