package com.company;

/**
 * https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
 */

class TreeNode
{
    TreeNode left;
    TreeNode right;
    int val;
    public TreeNode(int val)
    {
        this.val = val;
    }
}

public class PrintMaxDepthTree
{
    public static int maxDepth(TreeNode root)
    {
        if (root == null)
            return 0;

        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }

    public static void printMaxDepthTreeMain()
    {

    }

}
