using System;

// http://www.geeksforgeeks.org/merge-sort/
// named Solution.

class MergeSortSolution
{
    static int[] arr;
    static void MergeSortSolutionMain(string[] args)
    {
        
        arr = new int[7] { 38, 27, 43, 3, 9, 82, 10 };
        Console.WriteLine("Original array");
        Print();
        Sort();
        Print();
    }
    
    static void Print()
    {
        Console.WriteLine("Printing arr");
        for (int i = 0; i < arr.Length; i++)
        {
            Console.Write(arr[i] + " ");
        }
        Console.WriteLine();
    }
    
    static void MergeSort(int[] aux, int low, int high)
    {
        if (low >= high)
        {
            return;
        }
        int mid = (low+high)/2;
        MergeSort(aux, low, mid);
        MergeSort(aux, mid+1, high);
        Merge(aux, low, mid, high);
        Print();
    }
    
    static void Merge(int[] aux, int low, int mid, int high)
    {
        for (int x = low; x <= high; x++)
        {
            aux[x] = arr[x];
        }
        
        int k = low;
        int i = low;
        int j = mid + 1;
        while (k <= high)
        {
            if (i > mid && j <= high)
            {
                arr[k] = aux[j];
               
                j++;
            }
            
            else if (i <= mid && j > high)
            {
                arr[k] = aux[i];
               
                i++;
            }
            
            else if (aux[i] <= aux[j])
            {
                arr[k] = aux[i];
               
                i++;
            }
            
            else if (aux[i] > aux[j])
            {
                arr[k] = aux[j];
               
                j++;
                
            }
            
            k++;
        }
    }
    
    static void Sort()
    {
        int n = arr.Length;
        int[] aux = new int[n];
        MergeSort(aux, 0, n-1);
    }
}
