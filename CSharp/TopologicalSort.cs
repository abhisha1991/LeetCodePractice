using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    /// <summary>
    /// Recursive implementation 
    /// https://www.youtube.com/watch?v=ddTC4Zovtbc
    /// http://www.geeksforgeeks.org/topological-sorting/
    /// This is used when designing build systems [to build one dll before another] depending on the dependency
    /// </summary>
    class TopologicalSort
    {
        static Dictionary<int, List<int>> DAG;
        static bool[] Visited;
        static int[] Stack;
        static int StackIdx = 0;
        public static void TopologicalSortMain()
        {
            Console.WriteLine("Enter number of vertices:");
            int n  = Int32.Parse(Console.ReadLine());
            Visited = new bool[n];
            for (int j =0; j<n; j++)
            {
                Visited[j] = false;
            }
            DAG = new Dictionary<int, List<int>>();
            Stack = new int[n];
            for (int i =0; i <n; i++)
            {
                Console.WriteLine("For vertex: " + i);

                Console.WriteLine("How many edges is this vertex connected to?");
                int m = Int32.Parse(Console.ReadLine());
                int j = 0;
                List<int> edges = new List<int>();
                while (j < m)
                {
                    Console.WriteLine("Enter directed edges");
                    int x = Int32.Parse(Console.ReadLine());
                    edges.Add(x);
                    j++;
                }

                DAG.Add(i, edges); 

            }

            TopoSort(n);
            for (int k =n-1; k>=0; k--)
            {
                Console.WriteLine(Stack[k]);
            }
            Console.ReadKey();
        }

        public static void TopoSort(int n)
        {
            for (int i =0; i<n; i++)
            {
                if (Visited[i] == false)
                    TopoSortUtil(i);
            }
        }

        public static void TopoSortUtil(int v)
        {
            Visited[v] = true;
            Console.WriteLine("Marked node:" + v + " as visited");
            foreach(var item in DAG[v])
            {
                if (Visited[item] == true) continue;
                else TopoSortUtil(item);

            }
            Stack[StackIdx++] = v;
        }


    }
}
