using System;
using System.Collections.Generic;
using System.Linq;

namespace Test
{
    /// <summary>
    /// https://codefights.com/interview/Bpdq6EYZ6MW586va3
    /// </summary>
    class ProductExceptSelf
    {
        public static int productExceptSelf(int[] nums, int m)
        {
            System.Numerics.BigInteger[] fResults = new System.Numerics.BigInteger[nums.Length];
            System.Numerics.BigInteger products = new System.Numerics.BigInteger(1);
            foreach (var item in nums)
            {
                if (item != 1)
                    products = products * item;
            }

            for (int i = 0; i < nums.Length; i++)
            {
                System.Numerics.BigInteger tempProd = products;
                fResults[i] = (tempProd / nums[i]) % m;
            }
            System.Numerics.BigInteger result = 0;
            fResults.ToList().ForEach(x => result = result + x);
            return Convert.ToInt32((result % m).ToString());

        }
        public static int productExceptSelf3(int[] nums, int m)
        {
            System.Numerics.BigInteger[] result = new System.Numerics.BigInteger[nums.Length];

            result[nums.Length - 1] = 1;
            for (int i = nums.Length - 2; i >= 0; i--)
            {
                result[i] = result[i + 1] * nums[i + 1];
            }

            System.Numerics.BigInteger left = 1;
            for (int i = 0; i < nums.Length; i++)
            {
                result[i] = result[i] * left;
                left = left * nums[i];
            }
            System.Numerics.BigInteger y = 0;
            result.ToList().ForEach(x => y = y + x);
            return Convert.ToInt32((y % m).ToString());
        }
        public static int productExceptSelf2(int[] nums, int m)
        {
            System.Numerics.BigInteger[] result = new System.Numerics.BigInteger[nums.Length];
            System.Numerics.BigInteger tmp = 1;
            for (int i = 0; i < nums.Length; i++)
            {
                result[i] = tmp;
                tmp *= nums[i];
            }
            tmp = 1;
            for (int i = nums.Length - 1; i >= 0; i--)
            {
                result[i] = (result[i] * tmp) % m;
                tmp *= nums[i];
            }
            System.Numerics.BigInteger finalResult = 0;
            result.ToList().ForEach(x => finalResult = finalResult + x);
            return Convert.ToInt32((finalResult % m).ToString());
        }

        public static void productExceptSelfMain()
        {
            List<int> array = new List<int>() { 37, 50, 50, 6, 8, 54, 7, 64, 2, 64, 67, 59, 22, 73, 33, 53, 43, 77, 56, 76, 59, 96, 64, 100, 89, 38, 64, 73, 85, 96, 65, 50, 62, 4, 82, 57, 98, 61, 92, 55, 80, 53, 80, 55, 94, 9, 73, 89, 83, 80 };
            productExceptSelf2(array.ToArray(), 67);
        }
    }
}
