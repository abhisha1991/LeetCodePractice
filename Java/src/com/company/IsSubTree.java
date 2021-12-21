package com.company;

/**
 * http://www.geeksforgeeks.org/check-if-a-binary-tree-is-subtree-of-another-binary-tree/
 */
public class IsSubTree
{
    static boolean result = false;
    public static boolean isSubtree(Tree<Integer> t1, Tree<Integer> t2)
    {
        if (t2 == null)
            return  true;

        if (t1 == null && t2 == null)
            return true;

        if (t1 == null || t2 == null)
            return false;

        if (t1.value == t2.value)
        {
            result = isSubtree(t1.left, t2.left) && isSubtree(t1.right, t2.right);
        }
        else
        {
            isSubtree(t1.left, t2);
            isSubtree(t1.right, t2);
        }

        return result;

    }

    public static void isSubTreeMain()
    {

        /*
        * t1:             t2:
       5              10
      / \            /  \
    10   7          4    6
   /  \            / \    \
  4    6          1   2   -1
 / \    \
1   2   -1
        *
        */
        /*Tree<Integer> t1 = new Tree<>(5);
        t1.left = new Tree<>(10);
        t1.right = new Tree<>(7);
        t1.left.left = new Tree<>(4);
        t1.left.right = new Tree<>(6);
        t1.left.left.left = new Tree<>(1);
        t1.left.left.right = new Tree<>(2);
        t1.left.right.right = new Tree<>(-1);

        Tree<Integer> t2 = new Tree<>(10);
        t2.left = new Tree<>(4);
        t2.right = new Tree<>(6);
        t2.left.left = new Tree<>(1);
        t2.left.right = new Tree<>(2);
        t2.right.left = new Tree<>(-1);
        */

        Tree<Integer> t1 = new Tree<>(1);
        t1.left = new Tree<>(2);
        t1.right = new Tree<>(2);

        Tree<Integer> t2 = null;
        isSubtree(t1,t2);

    }
}
