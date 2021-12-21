using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    /// <summary>
    /// https://codefights.com/interview/zRR9siWo5JjNWj3xX
    /// findFirstSubstringOccurrence
    /// </summary>
    class StrStr
    {
        public static int strStr(string s, string x)
        {
            int sLength = s.Length;
            int xLength = x.Length; 

            if (sLength == 0 || xLength == 0) return -1;

            if (xLength > sLength) return -1;

            if (sLength == xLength && s == x) return 0;

            if (sLength == xLength && s != x) return -1;
            
            for (int i =0; i < sLength; i++)
            {
                if (s[i] != x[0])
                    continue;

                int pos = i;
                int match = 0;
                // If the remaining characters of x are more than the remaining char of s
                if (xLength - 1 > sLength - (pos + 1))
                {
                    return -1;
                }
                for (int j =1; j < xLength; j++)
                {
                    if (x[j] == s[pos + j])
                    {
                        match = j;
                        continue;
                    }
                    else
                    {
                        break;
                    }          
                }

                // x is a substring of s
                if (match == xLength -1)
                {
                    return pos;
                }
            }

            // Not found
            return -1;
        }

        public static int findFirstSubstringOccurrence2(string s, string x)
        {
            if (x == "") return -1;
            return s.IndexOf(x);
        }

        public static int findFirstSubstringOccurrence(string s, string x)
        {
            int i = 0, j = 0;
            for (; i < s.Length; i++)
            {
                if (s[i] == x[j])
                {
                    j++;
                    if (j == x.Length) return i - j + 1;
                }
                else
                    j = 0;
            }
            return -1;

            //var str = Regex.Split(s, x);
            //return str.Length == 1 ? -1 : str[0].Length;
            //return s.IndexOf(x);
        }

        public static void strStrMain()
        {
            findFirstSubstringOccurrence("abc", "d");
            findFirstSubstringOccurrence("abc", "a");
            findFirstSubstringOccurrence("aBcDefghaBcdEFgh", "ghb");
            findFirstSubstringOccurrence("abc", "");

            strStr("abc", "d");
            strStr("abc", "a");
            strStr("aBcDefghaBcdEFgh", "ghb");
            strStr("abc", "");


        }
    }
}
