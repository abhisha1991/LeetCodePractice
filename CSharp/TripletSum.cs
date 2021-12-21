using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    /// <summary>
    /// https://codefights.com/interview/MZnrYnavhHmYEwZs8
    /// </summary>
    class TripletSum
    {
        private static bool tripletSum(int x, int[] a)
        {
            int arr_size = a.Length;
            // Fix the first element as A[i]
            for (int i = 0; i < arr_size - 2; i++)
            {
                // Fix the second element as A[j]
                for (int j = i + 1; j < arr_size - 1; j++)
                {
                    if (a[i] + a[j] > x) continue;
                    // Now look for the third number
                    for (int k = j + 1; k < arr_size; k++)
                    {
                        if (a[i] + a[j] + a[k] == x)
                        {
                            return true;
                        }
                    }
                }
            }

            // If we reach here, then no triplet was found
            return false;
        }

        private static bool tripletSum3(int x, int[] a)
        {
            Array.Sort(a);
            for (int i = 0; i < a.Length; i++)
            {
                int l = i + 1, r = a.Length - 1; //two pointers
                while (l < r)
                {
                    if (a[i] + a[l] + a[r] == x) return true;
                    else if (a[i] + a[l] + a[r] > x) r--;
                    else l++;
                }
            }
            return false;
        }

        /// <summary>
        /// Not working for few cases
        /// </summary>
        /// <param name="x"></param>
        /// <param name="a"></param>
        /// <returns></returns>
        private static bool tripletSum2(int x, int[] a)
        {
            int firstNumber, secondNumber, thirdNumber;
            Array.Sort(a);
            
            for (int i = 0; i < a.Length -1; i++)
            {
                int j = a.Length - 1; 
                firstNumber = a[i];
                int k = i + 1;
                while (k < j)
                {
                    secondNumber = a[j];
                    thirdNumber = a[k];
                    if (firstNumber + secondNumber + thirdNumber > x)
                    {
                        j--;
                        continue;
                    }
                    
                    if (firstNumber + secondNumber + thirdNumber == x) return true;
                    else k++;
                }

                //thirdNumber = x - firstNumber - secondNumber;

                //for (int p = 0; p <= a.Length; p++)
                //{
                //    if (p == i) continue;
                    
                //    if (thirdNumber == a[p]) return true;
                //}
            }

            return false;   
        }

        public static void tripletSumMain()
        {
            tripletSum(15, new int[] { 14, 1, 2, 3, 8, 15, 3 });
            tripletSum(10, new int[] { 1, 2, 4, 3, 6 });
            tripletSum(647, new int[] { 890, 479, 884, 926, 266, 261, 46, 779, 822, 856, 521, 928, 774, 135, 252, 676, 337, 335, 2, 738, 311, 975, 591, 357, 72, 81, 936, 146, 283 });
        }
    }
}
