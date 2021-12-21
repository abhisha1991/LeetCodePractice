using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;
namespace Test
{
    /// <summary>
    /// https://leetcode.com/problems/game-of-life/discuss/
    /// https://discuss.leetcode.com/topic/29054/easiest-java-solution-with-explanation
    /// </summary>
    class GameOfLife
    {
        /*

           m = 5
           n = 5
           1 0 1 0 0
           1 1 0 0 1
           1 0 0 1 0
           1 1 1 1 1
           0 0 0 1 0


           Any live cell with fewer than two live neighbors dies, as if caused by under-population.
           Any live cell with two or three live neighbors lives on to the next generation.
           Any live cell with more than three live neighbors dies, as if by over-population..
           Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

        */

        public static void GameOfLifeMain()
        {
            Console.WriteLine("Enter the grid dims");
            Console.WriteLine("Enter number of rows");
            string rows = Console.ReadLine();

            Console.WriteLine("Enter number of cols");
            string cols = Console.ReadLine();
            int m = Int32.Parse(rows);
            int n = Int32.Parse(cols);
            int[,] board = new int[m, n];

            Console.WriteLine("Enter the grid elements");
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    Console.WriteLine("Enter element with dims " + i + " " + j);
                    board[i, j] = Int32.Parse(Console.ReadLine());
                }
            }

            GameOfLifeHelper(board);
        }

        public static void GameOfLifeHelper(int[,] board)
        {
            int m = board.GetLength(0);
            int n = board.GetLength(1);
            List<int> alives = new List<int>() { 1, 3 }; // 01, 11 (next state, curr state) - all currently alive states
            List<int> deads = new List<int>() { 0, 2 }; // 10, 00 (next state, curr state) - all currently dead states
            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    int a = FindNbors(board, i, j, m, n, alives); // number of alive neighbors
                    Console.WriteLine("For cell with dim " + i + " " + j + ", " + "number of alive nbors:" + a);
                    // int d = FindNbors(board, i, j, m, n, deads); // could also get this from 8 - a
                    bool isAlive = (board[i, j] == alives[0] || board[i, j] == alives[1]);
                    // isAlive being true means that the last bit is 1 (01 or 11)
                    // isAlive being false means that the last bit is 0 (00 or 10)
                    BitArray ba = new BitArray(new int[] { board[i, j] });
                    int[] arr = new int[1];
                    bool nextLive = false;
                    if (isAlive)
                    {
                        if (a < 2 || a > 3)
                        {
                            // die
                        }
                        else if (a == 2 || a == 3)
                        {
                            // live
                            nextLive = true;
                        }
                    }
                    else
                    {
                        if (a == 3)
                        {
                            // live
                            nextLive = true;
                        }
                    }
                    if (nextLive)
                    {
                        ba[1] = nextLive;
                        ba.CopyTo(arr, 0);
                        board[i, j] = arr[0];
                    }

                }
            }

            // set the next board
            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    board[i, j] = board[i, j] >> 1;
                }
            }

            // display
            Console.WriteLine("The next board is");
            for (int i = 0; i < m; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    Console.Write(board[i, j] + " ");
                }

                Console.WriteLine();
            }
        }

        private static int FindNbors(int[,] board, int i, int j, int m, int n, List<int> val)
        {
            int count = 0;
            int minX = Math.Max(i - 1, 0);
            int maxX = Math.Min(i + 1, m - 1);
            int minY = Math.Max(j - 1, 0);
            int maxY = Math.Min(j + 1, n - 1);
            for (int x = minX; x <= maxX; x++)
            {
                for (int y = minY; y <= maxY; y++)
                {
                    if (val.Contains(board[x, y]))
                    {
                        count++;
                    }
                }
            }

            // get only surrounding states, not the state of the cell under investigation
            if ((board[i, j] == 1 || board[i, j] == 3) && (val[0] == 1))
            {
                count--;
            }

            return count;

        }
    }
}
