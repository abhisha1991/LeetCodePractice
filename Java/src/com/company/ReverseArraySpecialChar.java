package com.company;

import java.util.ArrayList;

/**
 * http://www.geeksforgeeks.org/reverse-an-array-without-affecting-special-characters/
 */
public class ReverseArraySpecialChar
{
    public static char[] reverseArraySpecialChar(String arr)
    {
        int a = (int)'a';
        int z = (int)'z';
        int A = (int)'A';
        int Z = (int)'Z';

        char[] array = arr.toCharArray();
        int j = array.length - 1;
        int i = 0;
        for (; i < array.length/2 && j >= array.length/2;)
        {
            boolean ichar = (((int)array[i] >= a && (int)array[i] <=z) || ((int)array[i] >= A && (int)array[i] <= Z));
            boolean jchar = (((int)array[j] >= a && (int)array[j] <=z) || ((int)array[j] >= A && (int)array[j] <= Z));

            if (ichar && jchar)
            {
                char temp = array[i];
                array[i] = array[j];
                array[j] = temp;
                i++;
                j--;
                continue;
            }

            if (ichar && !jchar)
            {
                j--;
                continue;
            }

            if (!ichar && jchar)
            {
                i++;
                continue;
            }

            if (!ichar && !jchar)
            {
                i++;
                j--;
            }
        }
        System.out.println(array);
        return array;
    }

    public static void reverseArraySpecialCharMain()
    {
        reverseArraySpecialChar("Ab,c,de!$");
        reverseArraySpecialChar("aaaa[[[[b");
        reverseArraySpecialChar("2324535");
        reverseArraySpecialChar("23s2453f5a");
        reverseArraySpecialChar("ab");
        reverseArraySpecialChar("a1b");
        int x = 1;
    }


}
