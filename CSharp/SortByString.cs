using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    /// <summary>
    /// https://codefights.com/interview/myCQFF3mJ9nx7z6cJ
    /// </summary>
    class SortByString
    {
        
        public static string sortByString(string s, string t)
        {
            string newstr = string.Empty;
            foreach (var c in t)
            {
                int countOfC = s.Where(x => x == c).Count();
                if (countOfC == 0)
                    continue;
                for (int i=0; i < countOfC; i++)
                {
                    newstr = newstr + c;
                }

                s = s.Replace(c, '#');
            }

            foreach (var item in s)
            {
                if (item != '#')
                {
                    newstr = newstr + item;
                }
            }

            return newstr;
        }
        public static void sortByStringMain()
        {
            sortByString("good", "odg");
        }

    }
}
