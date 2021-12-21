using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    public class BST<T>
    {
        public BST(T val, int index)
        {
            this.Value = val;
            this.Index = index;
            this.SmallerCount = 0;
        }

        public BST<T> Left { get; set; }
        public BST<T> Right { get; set; }
        public T Value { get; set; }
        public int Index { get; set; }
        public int SmallerCount { get; set; }

    }

    /// <summary>
    /// https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
    /// </summary>
    class CountSmallerAfterNumber
    {
        static CountSmallerAfterNumber cs = new Test.CountSmallerAfterNumber();
        static int count;
        public static void countSmallerMain()
        {
            cs.CountSmaller(new int[] { 5, 2, 6, 1 });
        }

        BST<int> tree = null;
        SortedDictionary<int, int> result = new SortedDictionary<int, int>();
        public IList<int> CountSmaller(int[] nums)
        {
            int[] finalResult = new int[nums.Length];
            if (nums.Length == 0) return finalResult;

            tree = new BST<int>(nums[0], 0);
            for (int i = 1; i < nums.Length; i++)
            {
                AddElement(tree, nums[i], i);
            }

            var root = tree;

            PreOrder(root);

            foreach (var item in result.Keys)
            {
                finalResult[item] = result[item];
            }

            return finalResult;
        }

        public void PreOrder(BST<int> root)
        {
            if (root == null)
            {
                return;
            }
            count = 0;
            CountSubTree(root.Value, root.Index, tree);
            root.SmallerCount = count;
            if (!result.Keys.Contains(root.Index))
            {
                result.Add(root.Index, root.SmallerCount);
            }
            PreOrder(root.Left);
            PreOrder(root.Right);
        }

        public bool AddElement(BST<int> tree, int val, int pos)
        {
            if (tree == null) return false;
            if (tree.Left == null && val < tree.Value)
            {
                tree.Left = new BST<int>(val, pos);
                return true;
            }

            if (tree.Right == null && val >= tree.Value)
            {
                tree.Right = new BST<int>(val, pos);
                return true;
            }

            if (val >= tree.Value) return AddElement(tree.Right, val, pos);
            else return AddElement(tree.Left, val, pos);
        }

        public void CountSubTree(int val, int index, BST<int> tree)
        {
            if (tree == null)
                return;

            if (index < tree.Index && val > tree.Value) count++;

            CountSubTree(val, index, tree.Left);
            CountSubTree(val, index, tree.Right);
        }

    }
}
