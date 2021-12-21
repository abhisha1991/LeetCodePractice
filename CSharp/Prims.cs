using System;
using System.Text;
using System.Linq;
using System.Collections.Generic;

public class edge
{
	public char Source { get; set; }
	public char Dest { get; set; }
	public int Weight { get; set; }
}

// http://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/
// https://www.youtube.com/watch?v=cplfcGZmX7I
public class Prims
{
	public static Dictionary<edge, int> Edgs = new Dictionary<edge, int>();
	public static List<char> Vertices = new List<char>();
	public static List<char> Visited = new List<char>();
	public static Dictionary<char, List<char>> Nbors = new Dictionary<char, List<char>>();
	public static void PrimsMain(string[] args)
	{
		Console.WriteLine("Enter # of vertices:");
		int n = Int32.Parse(Console.ReadLine());
		int  i=0;
		while (i < n)
		{
			Console.WriteLine("Vertex " + i);
			Vertices.Add(Char.Parse(Console.ReadLine()));
			i++;
		}
		Console.WriteLine("Enter # of edges:");
		n = Int32.Parse(Console.ReadLine());
		if (n < Vertices.Count - 1) { throw new Exception(); }
		i =0;
		while (i < n)
		{
			Console.WriteLine("Edge " + i);
			var e = new edge();
			Console.WriteLine("Source");
			e.Source = Char.Parse(Console.ReadLine());
			
			Console.WriteLine("Destination");
			e.Dest = Char.Parse(Console.ReadLine());
			
			Console.WriteLine("Weight");
			e.Weight = Int32.Parse(Console.ReadLine());
			
			Edgs.Add(e, e.Weight);
			i++;
		}
		char start = Vertices[0];
		Visited.Add(start);
		
		i = 0;
		int sum = 0;
		while (Visited.Count < Vertices.Count)
		{
			bool flag = false;
			var nborList = Edgs.Where(x => Visited.Contains(x.Key.Source) ||  Visited.Contains(x.Key.Dest)).ToList();
			List<int> weights = new List<int>();
			foreach (var item in nborList)
			{
				weights.Add(item.Value);
			}
			weights.Sort();
			int min = weights.First();
			List<edge> edges = new List<edge>();
			foreach (var item in nborList)
			{
				edges.Add(item.Key);
			}
			edge e = edges.Where(x => x.Weight == min).First();
			if (!Visited.Contains(e.Source))
			{
				flag = true;
				Visited.Add(e.Source);
			}
			if (!Visited.Contains(e.Dest))
			{
				flag = true;
				Visited.Add(e.Dest);
			}
			
			if (flag)
			{	
				Console.WriteLine("Edge Added: " + e.Source + " " + e.Dest);
				sum += min;
			}
			Edgs.Remove(e);
		}
		
		Console.WriteLine("MST is:" + sum);
	}
	
}