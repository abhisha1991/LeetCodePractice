using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    class SortingAlgos
    {
        public static int[] insertionSort(int[] array)
        {
            if (array.Length == 1) { return array; }

            int indexEndOfSorted = 0;
            int indexBeginOfUnsorted = 1;

            while (indexBeginOfUnsorted != array.Length)
            {
                int toInsert = array[indexBeginOfUnsorted];
                for (int i = indexEndOfSorted; i >= 0; i--)
                {
                    if (toInsert < array[i])
                    {
                        array[i + 1] = array[i];
                        array[i] = toInsert;
                        continue;
                    }
                    if (toInsert >= array[indexEndOfSorted])
                    {
                        // Do nothing, already sorted in inc order
                        continue;
                    }
                    if (toInsert >= array[i])
                    {

                    }
                   
                }
                indexEndOfSorted++;
                indexBeginOfUnsorted++;
            }
            return array;
        }

        public static int[] selectionSort(int[] array)
        {
            int sortedIndex = 0;
         
            for (int x = 0; x < array.Length; x++)
            {
                int min = array[x];
                int pos = x;
                for (int i = sortedIndex; i < array.Length; i++)
                {
                    if (array[i] < min)
                    {
                        min = array[i];
                        pos = i;
                    }
                }
                // Found the min, swap with the sorted Index
                if (pos != sortedIndex)
                {
                    int temp = array[sortedIndex];
                    array[sortedIndex] = min;
                    array[pos] = temp;
                }

                sortedIndex++;
            }
            return array;
        }

        public static void sortingAlgosMain()
        {
            selectionSort(new int[10] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 });
            selectionSort(new int[10] { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 });
            insertionSort(new int[10] { 23, 15, 16, 8, 43, 12, 4, 1, 8, 2 });
            insertionSort(new int[10] { 101, -1, 12, 546, -0, 34, 1, 345, 456, 23 });
            insertionSort(new int[10] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 });
            insertionSort(new int[10] { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 });
            
        }

    }
}
