using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    /// <summary>
    /// https://discuss.leetcode.com/topic/31162/mergesort-solution/11
    /// Someone else's solution, more efficient apparently
    /// </summary>
    class CountSmallerAfterNumber2
    {
        static CountSmallerAfterNumber2 cs = new CountSmallerAfterNumber2();
        public static void CountSmallerAfterNumber2Main()
        {
            cs.countSmaller(new int[] { 5, 2, 6, 1 });
        }

        public List<int> countSmaller(int[] nums)
        {
            NumberIndex[] cnums = new NumberIndex[nums.Length];
            for (int i = 0; i < nums.Length; i++)
            {
                cnums[i] = new NumberIndex(nums[i], i);
            }
            int[] smaller = new int[nums.Length];
            cnums = sort(cnums, smaller);
            List<int> res = new List<int>();
            foreach (int i in smaller)
            {
                res.Add(i);
            }
            return res;
        }

        private NumberIndex[] sort(NumberIndex[] nums, int[] smaller)
        {
            int half = nums.Length / 2;
            if (half > 0)
            {
                int i = 0 ;
                NumberIndex[] rightPart = new NumberIndex[nums.Length - half];
                NumberIndex[] leftPart = new NumberIndex[half];
                for (i = 0; i < leftPart.Length; i++)
                {
                    leftPart[i] = new NumberIndex(nums[i]);
                }

                for (i = 0; i < rightPart.Length; i++)
                {
                    rightPart[i] = new NumberIndex(nums[half + i]);
                }

                NumberIndex[] left = sort(leftPart, smaller), right = sort(
                        rightPart, smaller);
                int m = left.Length, n = right.Length;
                i = 0; 
                int j = 0;
                while (i < m || j < n)
                {
                    if (j == n || i < m && left[i].number <= right[j].number)
                    {
                        nums[i + j] = left[i];
                        smaller[left[i].index] += j;
                        i++;
                    }
                    else
                    {
                        nums[i + j] = right[j];
                        j++;
                    }
                }
            }
            return nums;
        }
    }

    public class NumberIndex
    {
        public int number;
        public int index;

        public NumberIndex(int number, int index)
        {
            this.number = number;
            this.index = index;
        }

        public NumberIndex(NumberIndex another)
        {
            this.number = another.number;
            this.index = another.index;
        }
    }

   

    
}
