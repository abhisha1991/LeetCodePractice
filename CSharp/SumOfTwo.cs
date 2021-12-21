using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    /// <summary>
    /// https://codefights.com/interview/qAL6AiSejoJZRNyox
    /// </summary>
    class SumOfTwo
    {
        private static bool sumOfTwo2(int[] a, int[] b, int v)
        {
            if (a.Length == 0 || b.Length == 0) return false;

            List<int> aList = a.ToList();
            aList.Sort();
            List<int> bList = b.ToList();
            bList.Sort();
            
            // a = SortingAlgos.insertionSort(a);
            // b = SortingAlgos.insertionSort(b);

            int mida = aList.Count / 2;
            int midb = bList.Count / 2;
            int vSample = aList[mida] + bList[midb];
            if (vSample == v) return true;

            bool sampleSmall = vSample < v ? true : false;
            switch (sampleSmall)
            {
                case true:
                    // Sample is smaller than actual value, find bigger values
                    for (int i = mida; i < a.Length; i++)
                    {
                        for (int j = midb + 1; j < b.Length; j++)
                        {
                            vSample = aList[i] + bList[j];
                            if (vSample == v) return true;
                        }
                    }
                    break;
                case false:
                    // Sample is bigger than actual value, find smaller values
                    for (int i = mida; i >= 0; i--)
                    {
                        for (int j = midb - 1; j >= 0; j--)
                        {
                            vSample = aList[i] + bList[j];
                            if (vSample == v) return true;
                        }
                    }
                    break;
            }

            return false;
        }
        private static bool sumOfTwo3(int[] a, int[] b, int v)
        {
            int lena = a.Length;
            int lenb = b.Length;
            bool s = lena > lenb;
            int bigLength = s ? lena : lenb;
            int smallLength = s ? lenb : lena;
            int[] c = new int[smallLength];
            for (int i = 0; i < smallLength; i++)
            {
                if (s)
                {
                    c[i] = v - b[i];
                    // If c[i] exists in a, then return true
                    if (SearchElement(c[i], a)) return true;
                }
                else
                {
                    c[i] = v - a[i];
                    // If c[i] exists in b, then return true
                    if (SearchElement(c[i], b)) return true;
                }

            }

            return false;
        }

        private static bool sumOfTwo(int[] a, int[] b, int v)
        {
            int len = a.Length + b.Length;
            List<int> c = new List<int>();
            for (int i = 0, j = 0; i < len; i++)
            {
                if (i < a.Length)
                    c.Add(a[i]);
                else
                    c.Add(b[j++]);
            }

            int[] temp = new int[b.Length];
            for (int  i = 0, j = a.Length; i < a.Length; i++, j++)
            {
                // int aVal = a[i];
                // int bValToSearch = v - aVal;
                if (b.Where(x => x == v - a[i]).Any()) return true;
                // temp[i] = bValToSearch; 

            }

            return false;
        }

        
        private static bool SearchElement(int value, int[] arrayToSearch)
        {
            return arrayToSearch.ToList().Contains(value);
        }

        public static void SumOfTwoMain()
        {
            int[] a = new int[3] { 1, 2, 3 };
            // int[] a = new int[0];
            int[] b = new int[4] { 10, 20, 30, 40 };
            sumOfTwo(a, b, 8);
        }


    }
}
