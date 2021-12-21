using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    class GridElement
    {
        public int xpos;
        public int ypos;
        public bool visited;

        public GridElement(int x, int y)
        {
            xpos = x;
            ypos = y;
            visited = false;
        }
    }

    /// <summary>
    /// https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem
    /// Working solution
    /// </summary>
    class ConnectedCellInAGrid
    {

        static List<GridElement> visitedGridElements = new List<GridElement>();
        static int result = 0;
        static int tempResult = 0;
        static void ConnectedCellInAGridMain(String[] args)
        {
            int n = Convert.ToInt32(Console.ReadLine());
            int m = Convert.ToInt32(Console.ReadLine());
            int[][] grid = new int[n][];
            for (int grid_i = 0; grid_i < n; grid_i++)
            {
                string[] grid_temp = Console.ReadLine().Split(' ');
                grid[grid_i] = Array.ConvertAll(grid_temp, Int32.Parse);
            }

            for (int i = 0; i < grid.Length; i++)
            {
                for (int j = 0; j < grid[i].Length; j++)
                {
                    // i or xpos is the row
                    // j or ypos is the col 
                    ParseNeighbors(grid, i, j, grid.Length, grid[i].Length);
                    if (tempResult > result)
                    {
                        result = tempResult;
                    }
                    tempResult = 0;
                }
            }

            Console.WriteLine(result);
        }

        public static void ParseNeighbors(int[][] grid, int xpos, int ypos, int maxRows, int maxCols)
        {
            if (grid[xpos][ypos] == 0)
            {
                return;
            }

            if (visitedGridElements.Where(k => k.xpos == xpos && k.ypos == ypos && k.visited == true).Count() > 0)
            {
                return;
            }

            var element = new GridElement(xpos, ypos);
            element.visited = true;
            visitedGridElements.Add(element);

            tempResult += 1;
            GridElement north = new GridElement(xpos - 1, ypos);
            GridElement south = new GridElement(xpos + 1, ypos);
            GridElement east = new GridElement(xpos, ypos + 1);
            GridElement west = new GridElement(xpos, ypos - 1);
            GridElement northeast = new GridElement(xpos - 1, ypos + 1);
            GridElement northwest = new GridElement(xpos - 1, ypos - 1);
            GridElement southeast = new GridElement(xpos + 1, ypos + 1);
            GridElement southwest = new GridElement(xpos + 1, ypos - 1);
            List<GridElement> neighbors = new List<GridElement>();
            neighbors.Add(north);
            neighbors.Add(south);
            neighbors.Add(west);
            neighbors.Add(east);
            neighbors.Add(northwest);
            neighbors.Add(northeast);
            neighbors.Add(southwest);
            neighbors.Add(southeast);
            foreach (var item in neighbors)
            {
                if (item.xpos < 0 || item.xpos >= maxRows || item.ypos < 0 || item.ypos >= maxCols)
                {
                    continue;
                }
                ParseNeighbors(grid, item.xpos, item.ypos, grid.Length, grid[item.xpos].Length);
            }

        }
    }
}



