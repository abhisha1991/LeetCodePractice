package com.company;

import sun.security.util.BitArray;
import sun.swing.BakedArrayList;

import java.nio.channels.NonReadableChannelException;
import java.util.ArrayList;
import java.util.List;

/**
 * https://codefights.com/interview-practice/task/FwAR7koSB3uYYsqDp
 * SOLUTIONS BELOW NOT WORKING!!
 */
public class FindProfession
{
    // partially works
    public static String findProfession2(int level, int pos)
    {
        pos = (pos-1) % (1 << level-1) + 1;
        final char engineer = 'e';
        final char doc = 'd';
        List<Character> elements = new ArrayList<>();
        elements.add(engineer);
        elements.add(doc);
        char ele;
        for (int i = 2; i <=level; i ++)
        {
            int size = elements.size();
            for (int j = size - 1; j >=0; j--)
            {
                ele =  elements.get(j);
                if (i == 2)
                {
                    elements.add(ele);
                    continue;
                }
                switch (ele)
                {
                    case engineer:
                        ele = doc;
                        break;
                    case  doc:
                        ele = engineer;
                        break;
                }
                elements.add(ele);
            }
        }
        ele = elements.get(pos - 1);
        switch (ele)
        {
            case engineer:
                return "Engineer";
            case doc:
                return "Doctor";
            default:
                return "";
        }
    }

    /*
    * If you normalize the position to be 0-based and look at the bits, when you compare those bits to the path from root to the wanted position,
    * you can see that each 0 means "go to left child" and each 1 means "go to right child".
    * A left child always has the same profession as parent and a right child always has a different profession.
      So in other words, if the number of 1's in the position is odd, it's a Doctor, if even it's an Engineer.
    * */

    public static String findProfession(int level, int pos)
    {
        pos = (pos-1) % (1 << level-1) + 1;
        String result = Integer.toBinaryString(pos);
        char[] arr = result.toCharArray();
        int count = 0;
        for (int i = 0; i < arr.length - 1; i++)
        {
            if (arr[i] == 1)
            {
                count++;
            }
        }
        if ((count % 2 == 0))
            return "Engineer";
        else
            return "Doctor";

    }

    public static void findProfessionMain()
    {
        findProfession(3,3);
    }
}
