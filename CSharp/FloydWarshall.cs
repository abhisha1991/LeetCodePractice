using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
// http://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm/
// https://www.youtube.com/watch?v=LwJdNfdLF9s
public class FloydWarshall
{
    public const int Inf = 100000; 
    public static int[,] distMatrix; 
    public static int[,] pathMatrix;
    public static void FloydWarshallMain(string[] args)
    {
        Console.WriteLine("Enter the number of vertices");
        string n = Console.ReadLine();
        int v = Int32.Parse(n);
        distMatrix = new int[v,v];
        pathMatrix = new int[v,v];
        for (int i = 0; i<v; i++)
        {
            for (int j = 0; j<v; j++)
            {
                if (i == j)
                {
                    distMatrix[i,j] = 0;
                    pathMatrix[i,j] = -1;
                }
                else
                {
                    distMatrix[i,j] = Inf;
                    pathMatrix[i,j] = Inf;
                }
            }   
        }
        
        for (int i = 0; i<v; i++)
        {
            for (int j = 0; j<v; j++)
            {
                if (i == j) continue;
                
                Console.WriteLine("Enter dist for edge: " + i + " connecting to " + j);
                string d = Console.ReadLine();
                if (d == "") continue;
                distMatrix[i,j] = Int32.Parse(d);
                
            }   
        }
        
        for (int i = 0; i<v; i++)
        {
            for (int j = 0; j<v; j++)
            {
                if (distMatrix[i,j] != Inf || distMatrix[i,j] != 0)
                {
                    pathMatrix[i,j] = i;                    
                }
            }   
        }
        
        for (int k = 0; k<v; k++)
        {
            for (int i = 0; i<v; i++)
            {
                for (int j = 0; j<v; j++)
                {
                    if (distMatrix[i,j] == Inf && (distMatrix[i,k] == Inf ||
                    distMatrix[k,j] == Inf)) continue;
                    if (distMatrix[i,j] > distMatrix[i,k] + distMatrix[k,j])
                    {
                        distMatrix[i,j] = distMatrix[i,k] + distMatrix[k,j];
                        pathMatrix[i,j] = pathMatrix[k,j];
                    }
                }
            }
        }
        
        for (int i = 0; i<v; i++)
        {
            for (int j = 0; j<v; j++)
            {   
                Console.WriteLine("Min Dist for edge: " + i + " connecting to " + j + " is " + distMatrix[i,j]);
            }   
        }
        
        for (int i = 0; i<v; i++)
        {
            for (int j = 0; j<v; j++)
            {   
                Console.WriteLine("Min Dist Path for edge: " + i + " connecting to " + j + " is " + PrintPath(pathMatrix, i, j));
            }   
        }
        
        
    }
    
    public static string PrintPath(int[,] pathMatrix, int i, int j)
    {
        List<int> result = new List<int>();
        result.Add(j);
        while(pathMatrix[i,j] != i)
        {
          result.Add(pathMatrix[i,j]);
          j = pathMatrix[i,j]; // old source is the new destination
          
        }
        
        result.Add(i);
        result.Reverse();
        string ans = "";
        foreach (var item in result)
        {
            ans += item + " ";
        }
        
        return ans;
    }
  
}