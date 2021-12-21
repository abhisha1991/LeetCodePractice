using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    /// <summary>
    /// https://codefights.com/interview/4e6LZSessGpKPx3uB
    /// </summary>
    class StringReformatting
    {

        public static string stringReformatting(string s, int k)
        {
            if (s.Length == 1)
            {
                if (s[0] != '-')
                {
                    return s;
                }
                else
                {
                    return string.Empty;
                }
            }

            string str = string.Empty;
            foreach(var item in s)
            {
                if (item != '-')
                {
                    str = str + item;
                }
            }

            int strLength = str.Length;

            var reversed = str.Reverse();
            string newstr = string.Empty;
            int i= 0;
            foreach (var c in reversed)
            {
                if (i % k == 0)
                {
                    newstr = newstr + '-';
                }
                newstr = newstr + c;
                i++;
            }

            string result = string.Empty;
            foreach(var item in newstr.Reverse())
            {
                result = result + item;
            }
            if (result[result.Length -1] == '-')
            {
                return result.Substring(0, result.Length - 1);
            }
            return result;
        }

        public static void stringReformattingMain()
        {
            stringReformatting("-", 1);
        }

    }
}
