package com.company;

/**
 * http://practice.geeksforgeeks.org/problems/longest-increasing-subsequence/0
 * http://www.geeksforgeeks.org/?p=12832
 */
import java.util.*;
import java.lang.*;
import java.io.*;

public class LIS {
    static int result = 0;
    public static void lisMain (String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        int[] A = null;
        int x = 0;
        result = 0;
        while (x < t)
        {
            int n = scan.nextInt();
            A = new int[n];
            for (int i = 0; i < n ; i++)
            {
                A[i] = scan.nextInt();
            }

            x++;
            longestSubSeq(A);
            System.out.println(result);
        }
    }

    // https://www.youtube.com/watch?v=CE2b_-XfVDk
    public static int longestSubSeq(int[] A)
    {
        int i,j;
        i = 1;
        j = 0;
        int[] lss = new int[A.length];
        for (int k =0; k< A.length; k ++)
        {
            // lss will atleast be 1 (individual elements)
            lss[k] = 1;
        }

        // j is the behind counter,
        // i is the element under consideration
        while(j < i && i < A.length)
        {

            if (A[j] < A[i])
            {
                // if jth ele is < ith ele, lss must be lss of j + 1
                // + 1 being the ith ele
                // or if ith ele's lss is bigger already, that is taken
                lss[i] = Math.max(lss[j] + 1, lss[i]);
                j++;
                if (i == j)
                {
                    j = 0;
                    i = i+1;
                }

                continue;
            }

            if (A[j] >= A[i])
            {
                j++;
                if (i == j)
                {
                    j = 0;
                    i = i+1;
                }
                continue;
            }
        }

        // return the largest number of the lss array
        int max = 0;
        for (int k =0; k < A.length; k++)
        {
            if (max < lss[k]) max = lss[k];
        }
        return max;

    }

    // This is wrong!!
    public static int longestSubSeq2(int[] A)
    {
        if (A.length == 0) return 0;

        if (A.length == 1)
        {
            return 1;
        }

        if (A.length ==  2)
        {
            if (A[0] >= A[1]) return 1;
            else return 2;

        }

        // guaranteed to be 3 len
        int len = A.length;
        int half = len/2;

        int[] aFirstHalf = new int[half];
        int[] aSecondHalf = new int[len - half];

        for (int i =0; i <half; i++)
        {
            aFirstHalf[i] = A[i];
        }
        int k = 0;
        for (int j =half; j <len; j++)
        {
            aSecondHalf[k++] = A[j];
        }
        int a = longestSubSeq(aFirstHalf);
        int b = longestSubSeq(aSecondHalf);
        result += a + b;
        System.out.println(result);
        return 0;
    }
}
