package com.company;

import javafx.stage.StageStyle;
import org.omg.PortableServer.RequestProcessingPolicy;

import java.util.ArrayList;
import java.util.List;

/**
 * http://www.geeksforgeeks.org/print-nodes-at-k-distance-from-root/
 */

class Node2
{
    int data;
    Node2 left, right;
    public Node2(int item)    {
        data = item;
        left = right = null;
    }
}
public class PrintKDistance
{
    static List<Integer> result = new ArrayList<>();
    public static void printKDistance(Node2 root, int k)
    {
        if (root == null)
            return;

        if (k == -1)
            return;

        if (k == 0)
        {
            result.add(root.data);
            System.out.println(root.data);
        }

        printKDistance(root.left, k -1);
        printKDistance(root.right, k -1);
    }

    public static void printKDistanceMain()
    {
        /* Constructed binary tree is
                1
              /   \
             2     3
            /  \   /
           4    5 8
        */
        Node2 root = new Node2(1);
        root.left = new Node2(2);
        root.right = new Node2(3);
        root.left.left = new Node2(4);
        root.left.right = new Node2(5);
        root.right.left = new Node2(8);

        printKDistance(root, 2);
    }


}
