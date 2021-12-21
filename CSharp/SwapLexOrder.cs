using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    class SwapLexOrder
    {
        private static string swapLexOrder(string str, int[][] pairs)
        {
            List<int[]> swapPairs = new List<int[]>();
            
            foreach (var item in pairs)
            {
                swapPairs.Add(item);
            }
            char largest = 'a';
            Parallel.ForEach(str, x => largest = x.CompareTo(largest) > 0 ? x : largest);
            List<string> strHistory = new List<string>();
            strHistory.Add(str);
            List<LexElement> lex = new List<LexElement>();
            for (int i =0; i < str.Length; i++)
            {
                lex.Add(new LexElement {
                    value = str[i],
                    originalPos = i,
                    finalPos = -1,
                });
            }
            return null;
        }
        
        public static void swapLexOrderMain()
        {
            swapLexOrder("abdc", new int[][] { new int[] { 1, 4 }, new int[] { 3, 4 } });
        }
    }

    class LexElement
    {
        public char preceedingValue { get; set; }

        public char nextValue { get; set; }

        public char value { get; set; }

        public int originalPos { get; set; }

        public int finalPos { get; set; }

        public List<int> posHistory { get; set; }

        public LexElement()
        {
            posHistory = new List<int>();
        }
    }
}
