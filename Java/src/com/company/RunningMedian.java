package com.company;

/**
 * https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem
 * https://www.youtube.com/watch?v=VmogG01IjYc&t=315s
 */
import java.io.*;
import java.lang.reflect.Array;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Heap
{
    public int[] heap;
    public int size;
    public int capacity;

    public Heap()
    {
        size = 0;
        capacity = 100;
        heap = new int[capacity];

    }

    public int getFirstElement()
    {
        return heap[1];
    }

    public int getLastElement()
    {
        return heap[size];
    }

    public int getLeftChildIndex(int parent)
    {
        return 2 * parent;
    }

    public int getRightChildIndex(int parent)
    {
        return (2 * parent) + 1;
    }

    public void readjustSize()
    {
        if (size == capacity)
        {
            int[] temp = new int[size];
            for (int i =1; i<= size; i++)
            {
                temp[i] = heap[i];

            }
            capacity = 2 * capacity;
            heap = new int[capacity];
            for (int i =1; i<= size; i++)
            {
                heap[i] = temp[i];

            }
        }
    }

    public void printHeap()
    {
        System.out.println("Printing the heap");
        for (int i =1; i<= size; i++)
        {
            System.out.println(heap[i]);
        }
    }

    public void insertIntoMinHeap(int data)
    {
        readjustSize();
        heap[++size] = data;
        // Bubble it to the top
        int curr = size;
        int parent = curr/2;
        if (size == 1) return;
        while (heap[parent] > heap[curr])
        {
            swap(parent, curr);
            curr = parent;
            parent = curr/2;
            if (curr ==  1) break;
        }
    }

    public void insertIntoMaxHeap(int data)
    {
        readjustSize();
        heap[++size] = data;
        // Bubble it to the top
        int curr = size;
        int parent = curr/2;
        if (size == 1) return;
        while (heap[parent] < heap[curr])
        {
            swap(parent, curr);
            curr = parent;
            parent = curr/2;
            if (curr ==  1) break;
        }
    }

    public void deleteFromMinHeap()
    {
        int parent = 1;
        swap(parent, size);
        size--;
        // Bubble down the top element to correct position
        int left = getLeftChildIndex(parent);
        int right = getRightChildIndex(parent);
        if (right > size)
        {
            if (left == size && heap[left] < heap[parent])
            {
                swap(parent, left);
                return;
            }
            if (left > size) return;
        }
        while (heap[parent] > heap[left] || heap[parent] > heap[right])
        {
            boolean leftSmaller = heap[parent] > heap[left];
            boolean rightSmaller =  heap[parent] > heap[right];
            boolean bothSmaller = leftSmaller && rightSmaller;
            int smallestIndex;
            if (bothSmaller)
            {
                if (heap[left] > heap[right])
                {
                    smallestIndex = getRightChildIndex(parent);
                }
                else smallestIndex = getLeftChildIndex(parent);
            }
            else if (leftSmaller)
            {
                smallestIndex = getLeftChildIndex(parent);
            }
            else smallestIndex = getRightChildIndex(parent);
            swap(parent, smallestIndex);
            parent = smallestIndex;
            left = getLeftChildIndex(parent);
            right = getRightChildIndex(parent);
            if (left > size || right > size) break;
        }
    }

    public void deleteFromMaxHeap()
    {
        int parent = 1;
        swap(parent, size);
        size--;
        // Bubble down the top element to correct position
        int left = getLeftChildIndex(parent);
        int right = getRightChildIndex(parent);
        if (right > size)
        {
            if (left == size && heap[left] > heap[parent])
            {
                swap(parent, left);
                return;
            }
            if (left > size) return;
        }
        while (heap[parent] < heap[left] || heap[parent] < heap[right])
        {
            boolean leftBigger = heap[parent] < heap[left];
            boolean rightBigger =  heap[parent] < heap[right];
            boolean bothBigger = leftBigger && rightBigger;
            int biggestIndex;
            if (bothBigger)
            {
                if (heap[left] < heap[right])
                {
                    biggestIndex = getRightChildIndex(parent);
                }
                else biggestIndex = getLeftChildIndex(parent);
            }
            else if (leftBigger)
            {
                biggestIndex = getLeftChildIndex(parent);
            }
            else biggestIndex = getRightChildIndex(parent);
            swap(parent, biggestIndex);
            parent = biggestIndex;
            left = getLeftChildIndex(parent);
            right = getRightChildIndex(parent);
            if (left > size || right > size) break;
        }
    }

    public void swap(int index1, int index2)
    {
        int temp = heap[index1];
        heap[index1] = heap[index2];
        heap[index2] = temp;
    }

}

// Pretty sure this works, however, CTCI says its the wrong answer
public class RunningMedian {
    static Heap minHeapofBiggerEle = new Heap();
    static Heap maxHeapOfSmallerEle = new Heap();

    public static void rebalanceHeaps()
    {
        if (maxHeapOfSmallerEle.size - minHeapofBiggerEle.size == -1)
        {
            // take the top element of minHeapofBiggerEle and insert that into maxHeapOfSmallerEle
            /* maxH   minH                                       maxH   minH
            *   2     3       size(maxH) - size(minH) = -1 ->      3     4
            * 1      4 5                                          1 2   5
            * */
            int data = minHeapofBiggerEle.getFirstElement();
            maxHeapOfSmallerEle.insertIntoMaxHeap(data);
            // Delete that element from the minHeapofBiggerEle
            minHeapofBiggerEle.deleteFromMinHeap();
        }
        else if (maxHeapOfSmallerEle.size - minHeapofBiggerEle.size == 2)
        {
            int data = maxHeapOfSmallerEle.getFirstElement();
            minHeapofBiggerEle.insertIntoMinHeap(data);
            maxHeapOfSmallerEle.deleteFromMaxHeap();

        }

    }

    public static void printMedian()
    {
        System.out.println("Median is");
        int size = maxHeapOfSmallerEle.size + minHeapofBiggerEle.size;
        if (size % 2 == 1)
        {
            // print the top element of the min heap
            System.out.println(maxHeapOfSmallerEle.getFirstElement());
        }
        else
        {
            // print the average of the top element of max heap and the top element of min heap
            float f = (float) (maxHeapOfSmallerEle.getFirstElement() + minHeapofBiggerEle.getFirstElement())/2;
            System.out.println(f);
        }
    }
    public static void runningMedianMain() {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
            if (maxHeapOfSmallerEle.size == 0 || maxHeapOfSmallerEle.getFirstElement() > a[a_i])
            {
                maxHeapOfSmallerEle.insertIntoMaxHeap(a[a_i]);
            }
            else
            {
                minHeapofBiggerEle.insertIntoMinHeap(a[a_i]);
            }
            rebalanceHeaps();
            printMedian();
            if (a_i !=0 && a_i % 10 == 0)
            {
                int s = a_i + 1;
                int[] b = new int[s];
                for (int x =0; x<s; x++)
                {
                    b[x] = a[x];
                }
                Arrays.sort(b);
                System.out.println("Printing the array up till now");
                for (int x =0; x <s; x++)
                {
                    System.out.print(b[x] + " ");
                }
                double median = 0;
                if (b.length % 2 == 0)
                    median = ((double)b[b.length/2] + (double)b[b.length/2 - 1])/2;
                else
                    median = (double) b[b.length/2];
                System.out.println();
                System.out.println("ACTUAL Median is " + median);
                System.out.println("End of printing the array");
            }
        }
    }
}

