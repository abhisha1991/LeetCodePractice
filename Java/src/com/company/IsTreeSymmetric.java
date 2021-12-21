package com.company;

import java.util.ArrayList;
import java.util.List;
import java.util.ResourceBundle;

/**
 * https://codefights.com/interview-practice/task/tXN6wQsTknDT6bNrf
 * http://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/
 * http://blog.codefights.com/istreesymmetric-solution/
 */

public class IsTreeSymmetric
{
    static List<Integer> result = new ArrayList<>();
    public static boolean isTreeSymmetric(Tree<Integer> t)
    {
        if (t == null)
            return true;

        isTreeSymmetric(t.left);
        result.add(t.value);
        isTreeSymmetric(t.right);

        int j = result.size() - 1;
        for (int i = 0; i < result.size()/2; i++)
        {
            if (result.get(i) != result.get(j))
            {
                return false;
            }

            j--;
        }
        return true;
    }

    public  static  void isTreeSymmetricMain()
    {
        /*
         1
        / \
       2   2
      / \ / \
     3  4 4  3
         */
        Tree<Integer> t = new Tree<>(1);
        t.left = new Tree<>(2);
        t.right = new Tree<>(2);
        t.left.left = new Tree<>(3);
        t.left.right = new Tree<>(4);
        t.right.left = new Tree<>(4);
        t.right.right = new Tree<>(3);

        isTreeSymmetric(t);
    }
}
