package com.company;
import java.util.*;
/**
 * Created by abhisha on 10/14/2017.
 */
class HeapSort
{
    static int size;
    static int[] heap;
    static int currSize;
    static int[] arr;
    public static void main(String[] args)
    {
        System.out.println("Welcome to heapsort, enter n, then n integers");
        Scanner sc = new Scanner(System.in);
        size = sc.nextInt();
        currSize = 0;
        heap = new int[size+1];
        for (int i = 1; i <= size; i++)
        {
            int x = sc.nextInt();
            insertIntoHeap(x, i);
        }
        printHeap();
        System.out.println();
        System.out.println("Sorting the heap");
        sort();
        for (int i=0; i<currSize;i++)
        {
            System.out.println(arr[i]);
        }

    }

    public static void insertIntoHeap(int x, int idx)
    {
        heap[idx] = x;
        currSize++;
        if (idx == 1) return;
        int pIdx = getParentIndex(idx);
        while (heap[pIdx] > heap[idx])
        {
            swap(pIdx, idx);
            idx = pIdx;
            if (idx == 1) break;
            pIdx = getParentIndex(idx);
        }
    }

    public static void sort()
    {
        arr = new int[currSize];
        int i = 0;
        while (i < currSize)
        {
            swap(1, currSize - i);
            arr[i] = heap[currSize - i];
            heapify(currSize - i - 1);
            i++;
        }

    }

    public static void heapify(int h)
    {
        int parent = 1;
        int lc = getLeftChildIndex(parent);
        int rc = getRightChildIndex(parent);
        if (rc > h && lc > h)
        {
            return;
        }

        if (rc > h && lc == h)
        {
            if (heap[parent] > heap[lc])
            {
                swap(parent, lc);
            }
            return;
        }

        while (parent <= h && lc <=h && rc <=h && (heap[parent] > heap[lc] || heap[parent] > heap[rc]))
        {
            boolean isLeftSmaller = heap[parent] > heap[lc];
            boolean isRightSmaller = heap[parent] > heap[rc];
            boolean bothSmaller = isLeftSmaller && isRightSmaller;

            if (bothSmaller)
            {
                if (heap[lc] <= heap[rc]) isRightSmaller = false;
                else isLeftSmaller = false;
            }
            if (isLeftSmaller)
            {
                swap(parent, lc);
                parent = lc;
                lc = getLeftChildIndex(parent);
                rc = getRightChildIndex(parent);
            }
            else if (isRightSmaller)
            {
                swap(parent, rc);
                parent = rc;
                lc = getLeftChildIndex(parent);
                rc = getRightChildIndex(parent);
            }

        }
    }

    public static int getRoot()
    {
        return heap[1];
    }


    public static int getLeftChildIndex(int i)
    {
        return 2*i;
    }

    public static int getRightChildIndex(int i)
    {
        return 2*i + 1;
    }

    public static int getParentIndex(int i)
    {
        if (i ==1) return 1;

        return i/2;
    }

    public static void printHeap()
    {
        System.out.println("Printing the heap");
        for (int i=1; i<=currSize; i++)
        {
            System.out.print(heap[i]);
            System.out.print(' ');
        }
        System.out.println();

    }

    public static void swap(int i, int j)
    {
        int temp;
        temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;

    }

}


