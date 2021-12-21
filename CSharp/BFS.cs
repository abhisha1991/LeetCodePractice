using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    using System;
    using System.Collections.Generic;
    using System.IO;
    class Node
    {
        public int NodeId;
        public bool IsStart;
        public int DistanceFromStart;
        public List<Node> OtherConnectedNodes;
        public bool IsVisited;

        public Node(int id)
        {
            this.IsVisited = false;
            this.NodeId = id;
            this.IsStart = false;
            this.DistanceFromStart = 9999;
            this.OtherConnectedNodes = new List<Node>();
        }
    }

    class BFS
    {
        const int dist = 6;
        static Dictionary<int, Node> nodeDic = new Dictionary<int, Node>();
        static List<int> queue = new List<int>();
        static int bfsIteration = 1;
        static int globalStartNode = 0;
        public static void BFSMain(String[] args)
        {

            int q = Int32.Parse(Console.ReadLine());
            int startnode = 0;
            for (int i = 0; i < q; i++)
            {
                nodeDic = new Dictionary<int, Node>();
                queue = new List<int>();
                bfsIteration = 1;
                globalStartNode = 0;
                string input = Console.ReadLine();
                int nodes = Int32.Parse(input.Split(' ')[0]);

                int edges = Int32.Parse(input.Split(' ')[1]);
                for (int j = 0; j < edges; j++)
                {
                    input = Console.ReadLine();
                    int first = Int32.Parse(input.Split(' ')[0]);
                    int second = Int32.Parse(input.Split(' ')[1]);
                    InsertEgdes(first, second);
                }

                startnode = Int32.Parse(Console.ReadLine());
                // Set start node
                SetStartNode(startnode);
                globalStartNode = startnode;
                // Fill in missing keys (like in an unconnected graph)
                for (int x =1; x <= nodes; x++)
                {
                    if (!nodeDic.ContainsKey(x))
                    {
                        nodeDic.Add(x, new Node(x));
                    }
                }

                // BFS from start node
                DoBFS(startnode);

                // Display every node's distance
                for (int k = 1; k <= nodes; k++)
                {
                    if (k == startnode) continue;
                    if (nodeDic[k].DistanceFromStart == 9999)
                    {
                        nodeDic[k].DistanceFromStart = -1;
                    }
                    Console.Write(nodeDic[k].DistanceFromStart + " ");
                }
                Console.WriteLine();
            }
        }

        public static void InsertEgdes(int first, int second)
        {
            if (!nodeDic.ContainsKey(first))
            {
                nodeDic.Add(first, new Node(first));
            }

            if (!nodeDic.ContainsKey(second))
            {
                nodeDic.Add(second, new Node(second));
            }

            nodeDic[first].OtherConnectedNodes.Add(nodeDic[second]);
            nodeDic[second].OtherConnectedNodes.Add(nodeDic[first]);

        }

        public static void SetStartNode(int startnode)
        {
            foreach (var key in nodeDic.Keys)
            {
                if (key == startnode)
                {
                    nodeDic[key].IsStart = true;
                    nodeDic[key].IsVisited = true;
                    nodeDic[key].DistanceFromStart = 0;
                }
            }
        }

        public static void DoBFS(int startnode)
        {
            foreach (var item in nodeDic[startnode].OtherConnectedNodes)
            {
                if (item.IsVisited) continue;

                if (item.DistanceFromStart > bfsIteration * dist)
                {
                    int dist1 = bfsIteration * dist;
                    var listOfdist2 = item.OtherConnectedNodes.Select(x => x.DistanceFromStart).Where(y => y > 0).ToList();
                    int dist2;
                    if (listOfdist2.Count == 0)
                    {
                        dist2 = 9999;
                    }
                    else
                    {
                        dist2 = listOfdist2.Min();
                    }
                    item.DistanceFromStart = Math.Min(dist1, 6 + dist2);
                    item.IsVisited = true;
                }
                if (queue.Contains(item.NodeId)) continue;
                if (item.NodeId == globalStartNode) continue;
                queue.Add(item.NodeId);

            }
            if (queue.Count == 0) return;

            int first = queue[0];
            queue.RemoveAt(0);
            bfsIteration++;
            DoBFS(first);
        }
    }
}
