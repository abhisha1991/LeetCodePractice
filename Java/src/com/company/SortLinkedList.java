package com.company;

import org.omg.CORBA.INTERNAL;

import java.util.PrimitiveIterator;

/**
 * http://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1
 */

class Node1<T>
{
    T value;

    public Node1(T x)
    {
        value = x;
    }

    Node1<T> next;
}

public class SortLinkedList {

    public static void linksort(Node1<Integer> head) throws Exception
    {

        Integer[] count = {0, 0, 0};

        Node1<Integer> cur = head;
        while (cur != null)
        {
          switch (cur.value)
          {
              case 0:
                  count[0]++;
                  cur = cur.next;
                  break;
              case 1:
                  count[1]++;
                  cur = cur.next;
                  break;
              case 2:
                  count[2]++;
                  cur = cur.next;
                  break;
              default:
                  throw new Exception("Cannot have values other than 0,1,2");
          }
        }

        Integer i = 0;
        cur = head;
        for (i = 0; i < count.length; i ++)
        {
            Integer j = 0;
            while (j < count[i])
            {
                cur.value = i;
                j++;
                cur = cur.next;
            }
        }
        cur = head;
        while (cur != null)
        {
            System.out.println(cur.value + " ");
            cur = cur.next;
        }
        return;
    }

    public static void sortLinkedListMain()
    {
        Node1<Integer> node = new Node1<Integer>(2);
        node.next = new Node1(0);
        node.next.next = new Node1(1);
        node.next.next.next = new Node1(1);
        node.next.next.next.next = new Node1(2);
        node.next.next.next.next.next = new Node1(1);
        node.next.next.next.next.next.next = new Node1(0);
        node.next.next.next.next.next.next.next = new Node1(1);
        try
        {
            linksort(node);
        }
        catch (Exception ex)
        {
            System.out.println(ex);
        }

    }
}
