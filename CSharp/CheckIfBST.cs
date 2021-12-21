using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    /// <summary>
    /// https://www.youtube.com/watch?v=MILxfAbIhrE&list=PLrmLmBdmIlpv_jNDXtJGYTPNQ2L1gdHxu&index=8
    /// </summary>
    /// <typeparam name="T"></typeparam>
    public class TreeNode<T>
    {
        public T Val { get; set; }
        public TreeNode<T> Left { get; set; }
        public TreeNode<T> Right { get; set; }

        public TreeNode(T val)
        {
            this.Val = val;
        }
    }

    public class CheckBST
    {
        public static void CheckBSTMain(string[] args)
        {
            TreeNode<int> t = new TreeNode<int>(100);
            t.Left = new TreeNode<int>(45);
            t.Left.Right = new TreeNode<int>(75);
            t.Left.Right.Left = new TreeNode<int>(60);
            t.Left.Left = new TreeNode<int>(40);
            t.Left.Left.Right = new TreeNode<int>(43);
            t.Left.Left.Left = new TreeNode<int>(22);
            t.Right = new TreeNode<int>(200);
            t.Right.Right = new TreeNode<int>(1110);
            Console.WriteLine(CheckIfBst(t, -10000, 10000));
        }
        public static bool CheckIfBst(TreeNode<int> t, int min, int max)
        {
            if (t == null) return true;
            if (t.Val <= min || t.Val > max) return false;
            return CheckIfBst(t.Left, min, t.Val) && CheckIfBst(t.Right, t.Val, max);
        }
    }
}
