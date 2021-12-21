package com.company;

import com.sun.prism.sw.SWPipeline;
import javafx.scene.Parent;

import java.lang.management.RuntimeMXBean;
import java.util.concurrent.TransferQueue;

/**
 * Created by abhisha on 9/19/2017.
 */
public class MinHeap
{
    static int capacity = 100;
    int size;
    static int[] heap;
    public MinHeap()
    {
        size = 0;
        this.heap = new int[capacity];
    }

    public void readjustSize()
    {
        if (size == capacity)
        {
            int[] temp = new int[capacity];
            for (int i = 1; i <= capacity; i++)
            {
                temp[i] = heap[i];
            }
            capacity = 2 * capacity;
            heap = new int[capacity];
            for (int i = 1; i <= size; i++)
            {
                heap[i] = temp[i];
            }
        }
    }

    public void insert(int data) throws Exception
    {
        readjustSize();
        size++;
        heap[size] = data;
        // Now place this in the right position
        int parent = size/2;
        int idx = size;
        if (size == 1) return;
        while (heap[parent] > heap[idx])
        {
            swap(parent, idx);
            idx = parent;
            if (idx == 1) break;
            parent = idx/2;
        }
    }

    public void deleteMin() throws Exception
    {
        swap(1, size);
        size--;
        int idx = 0;
        int parent = 1;
        if (getRightChildIndex(parent) > size)
        {
            if (getLeftChildIndex(parent) == size && heap[getLeftChildIndex(parent)] < heap[parent])
            {
                swap(parent, getLeftChildIndex(parent));
                return;
            }
            if (getLeftChildIndex(parent) > size) return;
        }
        while ((heap[parent] > heap[getLeftChildIndex(parent)] || heap[parent] > heap[getRightChildIndex(parent)]))
        {
            boolean leftSmaller = heap[parent] > heap[getLeftChildIndex(parent)];
            boolean rightSmaller = heap[parent] > heap[getRightChildIndex(parent)];
            boolean bothSmaller = leftSmaller && rightSmaller;

            if (bothSmaller)
            {
                idx = heap[getLeftChildIndex(parent)] < heap[getRightChildIndex(parent)]
                        ? getLeftChildIndex(parent) : getRightChildIndex(parent);
            }
            else
            {
                if (leftSmaller) idx = getLeftChildIndex(parent);
                else idx = getRightChildIndex(parent);
            }
            swap(idx, parent);
            parent = idx;
            if (getRightChildIndex(parent) > size || getLeftChildIndex(parent) > size)
            {
                break;
            }
        }
    }

    public int getLeftChildIndex(int currIndex)
    {
        return 2 * currIndex;
    }

    public int getRightChildIndex(int currIndex)
    {
        return  (2 * currIndex) + 1;
    }

    public int getSmallestElement()
    {
        return heap[1];
    }

    public void printHeap()
    {
        System.out.println("Printing the heap");
        for (int i = 1; i <= size; i++)
        {
            System.out.print(heap[i] + " ");
        }
        System.out.println();
    }

    public void swap(int index1, int index2) throws Exception
    {
        if(index1 > size || index2 > size)
        {
            throw new Exception("Cannot have index greater than heap size");
        }

        int temp = heap[index1];
        heap[index1] = heap[index2];
        heap[index2] = temp;
    }

    public static void minHeapMain() throws Exception
    {
        System.out.println("Starting next test");
        MinHeap h = new MinHeap();
        h.insert(1);
        h.printHeap();
        h.insert(2);
        h.printHeap();
        h.insert(3);
        h.printHeap();
        h.insert(4);
        h.printHeap();
        h.insert(5);
        h.printHeap();
        h.insert(6);
        h.printHeap();
        h.insert(7);
        h.printHeap();
        h.insert(8);
        h.printHeap();
        h.insert(9);
        h.printHeap();
        h.insert(10);
        h.printHeap();
        h.deleteMin();
        h.printHeap();
        h.insert(0);
        h.printHeap();

        System.out.println("Starting next test");
        // second test
        h = new MinHeap();
        h.insert(10);
        h.printHeap();
        h.insert(9);
        h.printHeap();
        h.insert(8);
        h.printHeap();
        h.insert(7);
        h.printHeap();
        h.insert(6);
        h.printHeap();
        h.insert(5);
        h.printHeap();
        h.insert(4);
        h.printHeap();
        h.insert(3);
        h.printHeap();
        h.insert(2);
        h.printHeap();
        h.insert(1);
        h.printHeap();
        h.deleteMin();
        h.printHeap();

        System.out.println("Starting next test");
        // third test
        h = new MinHeap();
        h.insert(1);
        h.printHeap();
        h.insert(-1);
        h.printHeap();
        h.insert(5);
        h.printHeap();
        h.deleteMin();
        h.printHeap();
        h.insert(100);
        h.printHeap();
        h.insert(4);
        h.printHeap();
        h.insert(4);
        h.printHeap();
    }
}
