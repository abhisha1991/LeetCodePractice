using System.Text;
using System.Linq;
using System.Collections.Generic;
using System.Threading.Tasks;
using System;

public class Edge
{
    public Vertex source {get;set;}
    public Vertex dest {get;set;}
    public int weight {get;set;}
    public bool visited {get;set;}
    
    public Edge()
    {
        this.source = new Vertex();
        this.dest = new Vertex();
    }
}

public class Vertex
{
    public char v {get;set;}
    public int rank {get;set;}
    public Vertex parent {get;set;}
    
    /// <summary>
    /// this function is the equivalent of make set
    /// </summary>
    public Vertex()
    {
        this.rank = 0;
        this.parent = this;
    }
}

/// <summary>
/// Disjoint set https://www.youtube.com/watch?v=ID00PMy0-vE
/// MST using Kruskals that uses Disjoint set concept - https://www.youtube.com/watch?v=fAuF0EuZVCk&t=395s
/// http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/
/// Union find using disjoint sets -  http://www.geeksforgeeks.org/union-find/
/// </summary>
public class Kruskals
{ 
    // These are important data structures, took a while to get these right
    // Map - vertex character to vertex class mapping
    // Edg - dictionary - edge to its corresponding weight mapping
    public static Dictionary<char, Vertex> Map = new Dictionary<char, Vertex>();
    public static Dictionary<Edge, int> Edg = new Dictionary<Edge, int>();
    public static void KruskalsMain(string[] args)
    {
        Console.WriteLine("Enter number of vertices you want");
        int n = Int32.Parse(Console.ReadLine());
        int  i = 0;
        while (i < n)
        {
            Vertex v = new Vertex();
            Console.WriteLine("Vertex name:");
            v.v =  Char.Parse(Console.ReadLine());
            Map.Add(v.v, v);    
            i++;
        }

        Console.WriteLine("Enter number of edges you want");
        n = Int32.Parse(Console.ReadLine());
        if (n < Map.Count - 1) { throw new Exception("Cant have number of edges less than vertices - 1"); }
        MakeGraph(n);
        var edgeList = Edg.Values.Select(x => x).ToList();
        edgeList.Sort();
        int mst = 0;
        // All MST vertices stored in vtx
        List<char> vtx = new List<char>();
        int count = edgeList.Count;
        for (int j = 0; j < count; j++)
        {
            // get smallest weight and remove it from list
            int wt = edgeList[0];
            edgeList.RemoveAt(0);
            var e = Edg.Keys.Where(x => x.visited == false && wt == x.weight).FirstOrDefault();
            if (e == null) { throw new Exception("Cannot find edge with weight " + wt); }
            // mark edge as visited
            e.visited = true;
            // find parents of edge nodes
            var src = e.source;
            var dst = e.dest;
            Vertex parentSrc = FindParent(src);
            Vertex parentDst = FindParent(dst);

            // Condition for a cycle in a graph - why? think!!
            // watch 1:00 to 1:30 https://www.youtube.com/watch?v=n_t0a_8H8VY
            // If there is a common vertex between the 2 subsets, then that vertex must be uniting them to form a closed loop
            if (parentSrc.v == parentDst.v) continue;
            Console.WriteLine("Src:" + src.v + " and Dst:" + dst.v + " are in MST");
            mst += e.weight;
            // do a union of the edge nodes
            parentSrc.parent = parentDst;
            if (!vtx.Contains(e.source.v))
                vtx.Add(e.source.v);
            if (!vtx.Contains(e.dest.v))
                vtx.Add(e.dest.v);
        }

        Console.WriteLine("MST is: " + mst);
    }
    
    public static Vertex FindParent(Vertex node)
    {
        Vertex parent = node.parent;
        if (parent == node)
        {
            return node;
        }
        return FindParent(parent);
    }

    public static void MakeGraph(int n)
    {   
        for (int i = 0; i <n; i++)
        {
            Console.WriteLine("For edge: " + i);
            Edge e = new Edge();
            Console.WriteLine("Source");
            char s = Char.Parse(Console.ReadLine());
            
            Console.WriteLine("Dest");
            char d = Char.Parse(Console.ReadLine());
            
            Console.WriteLine("Weight");
            int w = Int32.Parse(Console.ReadLine());
            
            e.source = Map[s];
            e.dest = Map[d];
            e.weight = w;
            Edg.Add(e, w);
        }


    }  
}