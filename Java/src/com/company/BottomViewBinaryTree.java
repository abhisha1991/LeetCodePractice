package com.company;

import org.omg.CORBA.TRANSACTION_REQUIRED;

import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.ResourceBundle;
import java.util.TreeMap;

/**
 * http://www.geeksforgeeks.org/bottom-view-binary-tree/
 * http://algorithms.tutorialhorizon.com/print-the-bottom-view-of-the-binary-tree/
 * https://dzone.com/articles/hashmap-vs-treemap-vs
 * https://www.youtube.com/watch?v=V7alrvgS5AI&t=615s
 */
class BottomViewTree<T>
{
    BottomViewTree<T> left;
    BottomViewTree<T> right;
    int level;
    T value;
    public  BottomViewTree(T val)
    {
        level = 0;
        value = val;
    }
}


public class BottomViewBinaryTree
{
    static ArrayList<BottomViewTree> q = new ArrayList<>();
    static TreeMap<Integer, ArrayList<Integer>> map = new TreeMap<>();
    public static void bottomViewBinaryTree(BottomViewTree<Integer> tree)
    {
        if (tree == null)
        {
            return;
        }

        ArrayList<Integer> list =  map.get(tree.level);
        if (list == null)
        {
            list = new ArrayList<>();
            list.add(tree.value);
            map.put(tree.level, list);
        }
        else
        {
            map.get(tree.level).add(tree.value);
        }

        if (tree.left != null)
        {
            tree.left.level = tree.level - 1;
            q.add(tree.left);
        }

        if (tree.right != null)
        {
            tree.right.level = tree.level + 1;
            q.add(tree.right);
        }
        while (!q.isEmpty())
        {
            BottomViewTree first = q.get(0);
            q.remove(0);
            bottomViewBinaryTree(first);
        }
    }

    public static void printMap()
    {
        for (int key : map.keySet())
        {
            System.out.println(map.get(key).get(map.get(key).size() - 1));
        }

    }

    public static void bottomViewBinaryTreeMain()
    {
        BottomViewTree<Integer> tree = new BottomViewTree<>(1);
        tree.left = new BottomViewTree<>(2);
        tree.right = new BottomViewTree<>(3);
        bottomViewBinaryTree(tree);
        /*
        *              20
                     /    \
                   8       22
                 /  \     / \
               5     3   4   25
                    / \
                  10    14
        *
        * */

        printMap();
        q.clear();
        map.clear();

        BottomViewTree<Integer> tree1 = new BottomViewTree<>(20);
        tree1.left = new BottomViewTree<>(8);
        tree1.right = new BottomViewTree<>(22);
        tree1.right.left = new BottomViewTree<>(4);
        tree1.right.right = new BottomViewTree<>(25);
        tree1.left.left = new BottomViewTree<>(5);
        tree1.left.right = new BottomViewTree<>(3);
        tree1.left.right.left = new BottomViewTree<>(10);
        tree1.left.right.right = new BottomViewTree<>(14);
        bottomViewBinaryTree(tree1);

        printMap();
        q.clear();
        map.clear();

        BottomViewTree<Integer> tree2 = new BottomViewTree<>(1);
        tree2.left = new BottomViewTree<>(2);
        tree2.right = new BottomViewTree<>(3);
        tree2.left.left = new BottomViewTree<>(4);
        tree2.left.right = new BottomViewTree<>(5);
        tree2.right.right = new BottomViewTree<>(7);
        tree2.left.left.left = new BottomViewTree<>(8);
        tree2.left.left.right = new BottomViewTree<>(9);
        bottomViewBinaryTree(tree2);
        printMap();
    }

}
