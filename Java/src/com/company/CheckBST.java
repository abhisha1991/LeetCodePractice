package com.company;

import java.util.ArrayList;

/**
 * https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem
 */

public class CheckBST
{
    public static ArrayList<Integer> list = new ArrayList<>();
    public static boolean checkBST(Node root)
    {
        if (root == null)
        {
            return true;
        }

        inorderBST(root);
        if (list.size() == 0) return true;

        int max = list.get(0);
        for (int i = 1; i < list.size(); i++)
        {
            if (list.get(i) <= max)
            {
                return false;
            }
            else
            {
                max = list.get(i);
            }
        }

        return true;
    }


    public static void inorderBST(Node root)
    {
        if (root == null)
        {
            return;
        }

        inorderBST(root.left);
        list.add(root.data);
        inorderBST(root.right);
    }
}
