package com.company;

import com.sun.javafx.image.IntPixelGetter;
import com.sun.org.apache.bcel.internal.generic.LUSHR;
import com.sun.xml.internal.ws.message.ByteArrayAttachment;
import javafx.scene.control.TableView;
import sun.reflect.generics.tree.VoidDescriptor;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.TreeMap;

/**
 * Created by abhisha on 9/22/2017.
 https://www.youtube.com/watch?v=eBdKNoW3VJg
 */
class LeftViewTree<T>
{
    LeftViewTree<T> left;
    LeftViewTree<T> right;
    T value;
    int level;
    public LeftViewTree(T val)
    {
        level = 0;
        value = val;
    }
}

public class LeftViewBinaryTree
{
    public static ArrayList<LeftViewTree> q = new ArrayList<>();
    public static TreeMap<Integer, ArrayList<Integer>> result = new TreeMap<>();
    public static void leftViewBinaryTree(LeftViewTree<Integer> tree)
    {
        if (tree == null)
        {
            return;
        }

        ArrayList<Integer> list = result.get(tree.level);
        if (list == null)
        {
            list = new ArrayList<>();
            list.add(tree.value);
            result.put(tree.level, list);
        }
        else
        {
            result.get(tree.level).add(tree.value);
        }

        if (tree.left != null)
        {
            tree.left.level = tree.level + 1;
            q.add(tree.left);
        }

        if (tree.right != null)
        {
            tree.right.level = tree.level + 1;
            q.add(tree.right);
        }

        while (!q.isEmpty())
        {
            LeftViewTree element = q.get(0);
            q.remove(0);
            leftViewBinaryTree(element);
        }

    }

    public static void printMap()
    {
        for (int key : result.keySet())
        {
            System.out.println(result.get(key).get(0));
        }
    }

    public static void leftViewBinaryTreeMain()
    {
        /*
        *
        *     1
            /   \
           2     3
            \
             4
              \
               5
                \
                 6
        * */
        LeftViewTree<Integer> tree = new LeftViewTree<>(1);
        tree.left = new LeftViewTree<>(2);
        tree.right = new LeftViewTree<>(3);
        tree.left.right = new LeftViewTree<>(4);
        tree.left.right.right = new LeftViewTree<>(5);
        tree.left.right.right.right = new LeftViewTree<>(6);

        leftViewBinaryTree(tree);
        printMap();
        q.clear();
        result.clear();

        /*
        *        1
               /   \
              2     3
             / \     \
            4   5     6
        *
        * */

        LeftViewTree<Integer> tree1 = new LeftViewTree<>(1);
        tree1.left = new LeftViewTree<>(2);
        tree1.right = new LeftViewTree<>(3);
        tree1.left.left = new LeftViewTree<>(4);
        tree1.left.right = new LeftViewTree<>(5);
        tree1.left.right = new LeftViewTree<>(6);


        leftViewBinaryTree(tree1);
        printMap();
        q.clear();
        result.clear();
    }
}
