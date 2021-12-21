package com.company;

import javax.sql.rowset.spi.TransactionalWriter;

/**
 * http://practice.geeksforgeeks.org/problems/minimum-depth-of-a-binary-tree/1
 */
public class MinDepthBinaryTree
{
    public static int minDepthBinaryTree(Tree<Integer> tree)
    {
        if (tree == null)
        {
            return 0;
        }

        return Math.min(1+ minDepthBinaryTree(tree.left), 1+ minDepthBinaryTree(tree.right));
    }


    public static void minDepthBinaryTreeMain()
    {
        Tree<Integer> tree = new Tree<>(1);
        tree.left = new Tree<>(3);
        tree.right = new Tree<>(2);

        minDepthBinaryTree(tree);

        Tree<Integer> tree1 = new Tree<>(10);
        tree1.left = new Tree<>(20);
        tree1.left.left = new Tree<>(40);
        tree1.left.right = new Tree<>(60);
        tree1.right = new Tree<>(30);

        int x = minDepthBinaryTree(tree1);
        System.out.println(x);
    }
}
