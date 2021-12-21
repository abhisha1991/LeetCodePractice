using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    /// <summary>
    /// http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
    /// </summary>
    class StringPermutation
    {
        static List<string> result { get; set; }

        static StringPermutation()
        {
            result = new List<string>();
        }

        /// <summary>
        /// With duplicates as well as without duplicates
        /// </summary>
        /// <param name="start"></param>
        /// <param name="end"></param>
        /// <param name="arr"></param>
        private static void stringPermutation(int start, int end, char[] arr)
        {
            if (start == end && !result.Contains(new string(arr))) result.Add(new string(arr));
            
            else
            {
                int i;
                for (i = start; i <= end; i++)
                {
                    arr = swap(start, i, arr);
                    stringPermutation(start + 1, end, arr);
                    arr = swap(start, i, arr); // Back track
                }
            }
           
        }
        
        private static char[] swap(int i, int j, char[] arr)
        {
            char temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            return arr;
        }
        
        public static void StringPermutationMain()
        {
            char[] arr = new char[] { 'a', 'b', 'c', 'c' };
            stringPermutation(0, arr.Length -1, arr);
            
            result.ForEach(x => Console.WriteLine(x + "\n"));
        }
    }
}
