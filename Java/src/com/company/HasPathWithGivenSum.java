package com.company;
import java.util.*;

/**
 * https://codefights.com/interview-practice/task/TG4tEMPnAc3PnzRCs/description
 * https://www.youtube.com/watch?v=Jg4E4KZstFE&list=PLrmLmBdmIlpv_jNDXtJGYTPNQ2L1gdHxu&index=7
 */
class Tree<T>
{
    T value;
    Tree<T> left;
    Tree<T> right;

    Tree(T x)
    {
        value = x;
    }
}
public class HasPathWithGivenSum
{
    public static ArrayList<Integer> arr = new ArrayList<>();
    public  static boolean hasPathWithGivenSum(Tree<Integer> t, int s)
    {
        if (t == null)
            return (s == 0);
        else
        {
            boolean ans = false;
            int subsum = s - t.value;
            // if we've found the sum and we're at a leaf
            if ((subsum == 0 && t.left == null && t.right == null))
            {
                arr.add(t.value);
                return true;
            }
            if (t.left != null)
            {
                boolean subres = hasPathWithGivenSum(t.left, subsum);
                ans = ans || subres;
                if (subres)
                {
                    arr.add(t.value);
                }
            }

            if (t.right != null)
            {
                boolean subres = hasPathWithGivenSum(t.right, subsum);
                ans = ans || subres;
                if (subres)
                {
                    arr.add(t.value);
                }
            }

            return ans;
        }

    }


    public  static  void hasPathWithGivenSumMain()
    {
        /*
        t: {
        "value": 5,
        "left": {
        "value": 7,
        "left": null,
        "right": null
        },
        "right": null
        }
        s: 5
        ***false***
        */

        /*
        t: {
        "value": 8,
        "left": null,
        "right": {
        "value": 8,
        "left": null,
        "right": null
        }
        }
        s: 16
        ***true***
        */
        Tree<Integer> t = new Tree<>(8);
        t.right = new Tree<>(8);

        PrintArrayIfExists(hasPathWithGivenSum(t,16));

        t = new Tree<>(8);
        t.right = new Tree<>(8);
        PrintArrayIfExists(hasPathWithGivenSum(t,17));

        t = new Tree<>(1);
        t.left = new Tree<>(2);
        t.right = new Tree<>(3);
        t.right.left = new Tree<>(4);
        t.right.right = new Tree<>(5);
        t.left.left = new Tree<>(7);
        t.left.right = new Tree<>(8);

        PrintArrayIfExists(hasPathWithGivenSum(t,9));
        PrintArrayIfExists(hasPathWithGivenSum(t,10));
        PrintArrayIfExists(hasPathWithGivenSum(t,11));
        PrintArrayIfExists(hasPathWithGivenSum(t,12));
    }

    static void PrintArrayIfExists(boolean ans)
    {
        if (ans)
        {
            System.out.println("Sum does exist");
            for(int i: arr)
            {
                System.out.println(i);
            }
        }

        arr.clear();
    }
}
