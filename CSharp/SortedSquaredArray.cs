using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    /// <summary>
    /// https://codefights.com/interview/GRGRoSLJnKKijH4vA
    /// </summary>
    class SortedSquaredArray
    {
        private static int[] sortedSquaredArray(int[] array)
        {
            if (array == null) return null;
            int len = array.Length;
            if (len == 0) return new int[0];
            if (len == 1) return new int[1] { array[0] * array[0] };
            
            int[] results = new int[len];
            int index = 0;
            foreach (var item in array)
            {
                results[index] = -1; // results only can store positive values
                array[index++] = item * item;
            }

            int count = 1;
            // Not a perfect looping condition, but works here as all elements have to be squared, so they cant be negative values
            for (int i = 0, j = len - 1; results[0] == -1;) 
            {
                if (array[i] > array[j])
                {
                    // head bigger than tail
                    results[len - count] = array[i];
                    i++;
                }
                else
                {
                    // tail bigger than head
                    results[len - count] = array[j];
                    j--;
                }
                count++;
            }

            return results;
        }


        public static void sortedSquaredArrayMain()
        {
            sortedSquaredArray(new int[] { -6, -4, 1, 2, 3, 5 });
            sortedSquaredArray(new int[] { -49, -48, -35, -34, -29, -25, -15, -12, -3, -1 });
        }
    }
}
