package com.company;

/**
 * Created by abhisha on 9/19/2017.
 */
public class MaxHeap
{
    public static int[] heap;
    static final int notAllocated = -1;
    public MaxHeap()
    {
       heap = new int[100];
       for (int i =0 ; i < heap.length; i++)
       {
           heap[i] = notAllocated;
       }
    }

    public void insert(int data)
    {
        if (heap[1] == notAllocated)
        {
            heap[1] = data;
            return;
        }
        int i = getLastValidIndex() + 1;
        heap[i] = data;
        int parent = i/2; // Always i/2 irrespective of left/right child

        while (heap[i] > heap[parent])
        {
            int temp = heap[parent];
            heap[parent] = heap[i];
            heap[i] = temp;
            i = parent;
            if (i == 1) break;
            parent = i/2;
        }
    }

    public int getMaxElement()
    {
        return heap[1];
    }

    public void deleteRoot()
    {
        int x = getLastValidIndex();
        int temp = heap[x];
        heap[x] = heap[1];
        heap[1] = temp;
        heap[x] = notAllocated;
        // After exchanging largest (first) element and last element
        // Bubble down this new root to its correct place
        int parent = 1;
        while (heap[parent] < heap[2* parent] || heap[parent] < heap[(2 * parent) +1])
        {
            boolean leftBigger = false;
            boolean rightBigger = false;
            int biggestIndex = 0;
            if (heap[parent] < heap[2* parent])
            {
                leftBigger = true;
            }
            if (heap[parent] < heap[(2 * parent) + 1])
            {
                rightBigger = true;
            }
            boolean bothBigger = leftBigger && rightBigger;
            if (bothBigger)
            {
                biggestIndex = heap[2 * parent] < heap[(2 * parent) + 1] ? (2 * parent) + 1 : 2 * parent;
            }
            else
            {
                biggestIndex = leftBigger ? 2 * parent : (2 * parent) + 1;
            }
            // Now you have the max of the three
            // swap parent and biggest index
            temp = heap[biggestIndex];
            heap[biggestIndex] = heap[parent];
            heap[parent] = temp;
            parent = biggestIndex;
        }
    }

    public int getLastValidIndex()
    {
        int i ;
        for (i = 1; heap[i] != -1; i++)
        {
            // do nothing
        }
        return i-1;
    }

    public void deleteLastElement()
    {
        heap[getLastValidIndex()] = notAllocated;
    }

    public void printHeap()
    {
        int len = getLastValidIndex();
        System.out.println("Printing the heap, it has " + len + " elements so far");
        for (int i =1; i <= len; i++)
        {
            System.out.print(heap[i] + " ");
        }
        System.out.println();
    }

    public  static void maxHeapMain()
    {
        MaxHeap h = new MaxHeap();
        h.insert(200);
        h.printHeap();
        h.insert(20);
        h.printHeap();
        h.insert(30);
        h.printHeap();
        h.insert(60);
        h.printHeap();
        h.insert(90);
        h.printHeap();
        h.insert(40);
        h.printHeap();
        h.insert(50);
        h.printHeap();
        h.insert(120);
        h.printHeap();
        h.insert(150);
        h.printHeap();
        h.insert(140);
        h.printHeap();
        h.deleteRoot();
        h.printHeap();
    }
}
