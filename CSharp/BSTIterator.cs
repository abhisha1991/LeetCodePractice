using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    using System;
    using System.Collections.Generic;
    using System.Linq;
    class Tree
    {
        public Tree Left;
        public Tree Right;
        public int val;
        public Tree(int v)
        {
            val = v;
        }
    }

    class BSTIteratorDriver
    {
        public static void BSTIteratorMain(String[] args)
        {
            /*
                   15
                 /    \
                10      25
                /\     /   \
               7  11  19    30
              /\     / \    / \
             5  8   18 23  29  32
                   /    \
                  17    24
            */
            Tree t = new Tree(15);
            t.Left = new Tree(10);
            t.Left.Right = new Tree(11);
            t.Left.Left = new Tree(7);
            t.Left.Left.Right = new Tree(8);
            t.Left.Left.Left = new Tree(5);
            t.Right = new Tree(25);
            t.Right.Left = new Tree(19);
            t.Right.Left.Right = new Tree(23);
            t.Right.Left.Right.Right = new Tree(24);
            t.Right.Left.Left = new Tree(18);
            t.Right.Left.Left.Left = new Tree(17);
            t.Right.Right = new Tree(30);
            t.Right.Right.Right = new Tree(32);
            t.Right.Right.Left = new Tree(29);
            Console.WriteLine("Performing Inorder Recursive");
            InOrder(t);
            Console.WriteLine("Performing Inorder Non-Recursive");
            NonRecInOrder(t);
            Nodes.Clear();
            Console.WriteLine("Performing Preorder Non-Recursive");
            NonRecPreOrder(t);
        }

        public static List<Tree> Nodes = new List<Tree>();

        /// <summary>
        /// LNR
        /// </summary>
        /// <param name="t"></param>
        public static void NonRecInOrder(Tree t)
        {
            Nodes.Add(t);
            t = t.Left;
            while (t != null || Nodes.Count > 0)
            {
                while (t != null)
                {
                    Nodes.Add(t);
                    t = t.Left;
                }
                int len = Nodes.Count - 1;
                t = Nodes.ElementAt(len);
                Console.WriteLine(t.val);
                Nodes.RemoveAt(len);
                t = (t.Right);
            }


        }

        /// <summary>
        /// NLR
        /// </summary>
        /// <param name="t"></param>
        public static void NonRecPreOrder(Tree t)
        {

            while (t != null || Nodes.Count > 0)
            {
                while (t != null)
                {
                    Nodes.Add(t);
                    Console.WriteLine(t.val);
                    t = t.Left;
                }
                int idx = Nodes.Count - 1;
                t = Nodes.ElementAt(idx);
                t = t.Right;
                Nodes.RemoveAt(idx);

            }
        }

        public static void InOrder(Tree root)
        {
            if (root == null)
            {
                return;

            }
            InOrder(root.Left);
            Console.WriteLine(root.val);
            InOrder(root.Right);
        }
    }
}
