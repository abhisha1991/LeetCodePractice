package com.company;

/**
 * http://www.geeksforgeeks.org/check-whether-binary-tree-full-binary-tree-not/
 */
public class FullBinaryTree
{
    public static boolean isFullBinaryTree(Tree<Integer> root)
    {
        if (root == null)
        {
            return true;
        }

        if (root.left != null && root.right == null)
        {
            return  false;

        }

        if (root.left == null && root.right != null)
        {
            return  false;

        }

        return isFullBinaryTree(root.left) && isFullBinaryTree(root.right);
    }

    public static void isFullBinaryTreeMain()
    {
        Tree<Integer> tree = new Tree<>(1);
        tree.left = new Tree<>(1);
        tree.right = new Tree<>(1);

        isFullBinaryTree(tree);
        Tree<Integer> root = new Tree<>(10);
        root.left = new Tree<>(20);
        root.right = new Tree<>(30);

        root.left.right = new Tree<>(40);
        root.left.left = new Tree<>(50);
        root.right.left = new Tree<>(60);
        root.right.right = new Tree<>(70);

        root.left.left.left = new Tree<>(80);
        root.left.left.right = new Tree<>(90);
        root.left.right.left = new Tree<>(80);
        root.left.right.right = new Tree<>(90);
        root.right.left.left = new Tree<>(80);
        root.right.left.right = new Tree<>(90);
        root.right.right.left = new Tree<>(80);
        root.right.right.right = new Tree<>(90);
        boolean x = isFullBinaryTree(root);
        System.out.println(x);
    }

}
