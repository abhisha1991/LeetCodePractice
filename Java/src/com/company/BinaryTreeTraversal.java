package com.company;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Queue;

/**
 * http://algorithms.tutorialhorizon.com/breadth-first-searchtraversal-in-a-binary-tree/
 */
public class BinaryTreeTraversal
{
    static ArrayList<Integer> arr = new ArrayList<>();

    public static void dfs(Tree<Integer> tree)
    {
        if (tree == null)
        {
            return;
        }

        dfs(tree.left);
        dfs(tree.right);
        // Post order - LRN
        arr.add(tree.value);
    }

    // BFS Also called level order search
    static ArrayList<Tree<Integer>> queue = new ArrayList<>();
    public static void bfs(Tree<Integer> tree)
    {
        if (tree == null)
        {
            return;
        }

        arr.add(tree.value);

        if (tree.left != null)
        {
            queue.add(tree.left);
        }

        if (tree.right != null)
        {
            queue.add(tree.right);
        }

        while (!queue.isEmpty())
        {
            Tree<Integer> remove = queue.remove(0);
            bfs(remove);
        }
    }

    public static void binaryTreeTraversalMain()
    {
        Tree<Integer> t = new Tree<>(1);
        t.left = new Tree<>(2);
        t.left.left = new Tree<>(4);
        t.left.right = new Tree<>(5);
        t.right = new Tree<>(3);

        dfs(t);
       /* for (int i : arr)
        {
            System.out.println(i);
        }*/
        arr.clear();
        Tree<Integer> t2 = new Tree<>(1);
        t2.left = new Tree<>(2);
        t2.right = new Tree<>(3);
        t2.left.left = new Tree<>(4);
        t2.left.right = new Tree<>(5);
        t2.right.left = new Tree<>(6);
        t2.right.right = new Tree<>(7);
        t2.left.left.left = new Tree<>(8);
        t2.left.left.right = new Tree<>(9);
        t2.left.right.left = new Tree<>(10);
        t2.left.right.right = new Tree<>(11);

        bfs(t2);
        /*for (int i : arr)
        {
            System.out.println(i);
        }
        */
        arr.clear();
        Tree<Integer> t3 = new Tree<>(1);
        t3.left = new Tree<>(2);
        t3.right = new Tree<>(3);
        t3.left.left = new Tree<>(4);
        t3.right.left = new Tree<>(5);
        t3.right.right = new Tree<>(6);

        bfs(t3);
        for (int i : arr)
        {
            System.out.println(i);
        }
    }
}
