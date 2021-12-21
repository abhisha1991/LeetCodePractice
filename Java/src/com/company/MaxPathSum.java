package com.company;

import javax.swing.text.StyledEditorKit;

/**
 * http://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/
 */
public class MaxPathSum
{
    public static int maxPathSum(Tree<Integer> tree)
    {
        if (tree == null)
        {
            return 0;
        }
        int maxsum = tree.value;
        int left = maxSubtreeSum(tree.left);
        if (left > 0)
        {
            maxsum += left;
        }

        int right = maxSubtreeSum(tree.right);
        if (right > 0)
        {
            maxsum += right;
        }

        return maxsum;
    }

    public static int maxSubtreeSum(Tree<Integer> subtree)
    {
        if (subtree == null)
        {
            return 0;
        }
        int maxsubtreeVal = Math.max(subtree.value + maxSubtreeSum(subtree.left), subtree.value + maxSubtreeSum(subtree.right));

        if(subtree.value > maxsubtreeVal)
        {
            return subtree.value;
        }

        else if (maxsubtreeVal < 0)
        {
            return 0;
        }

        else return maxsubtreeVal;
    }

    public static void maxPathSumMain()
    {
        Tree<Integer> t = new Tree<>(10);
        t.left = new Tree<>(-6);
        t.left.left = new Tree<>(1000);
        t.left.left.left = new Tree<>(-5000);
        t.left.right = new Tree<>(4);

        t.right = new Tree<>(15);

        maxPathSum(t);

        Tree<Integer> t1 = new Tree<>(10);
        t1.left = new Tree<>(-6);
        maxPathSum(t1);
    }

}
