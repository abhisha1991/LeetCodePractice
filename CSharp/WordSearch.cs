using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    public class BoardChar
    {
        public bool IsVisited { get; set; }
        public bool IsMatched { get; set; }
        public BoardChar North { get; set; }
        public BoardChar South { get; set; }
        public BoardChar East { get; set; }
        public BoardChar West { get; set; }
        public XY Pos { get; set; }
        public BoardChar()
        {
            this.Pos = new XY();
            this.IsVisited = false;
            this.IsMatched = false;
        }
    }

    public class XY
    {
        public int x { get; set; }
        public int y { get; set; }
    }

    /// <summary>
    /// https://leetcode.com/problems/word-search/description/
    /// https://paste.ofcode.org/FewGmEtNJyzZf7urtfV3Uw
    /// Wrong solution, wont work when we have multiple directions to go to and only one of them is eventually correct
    /// </summary>
    public class WordSearch
    {
        static int rows;
        static int cols;
        public static void wordSearchMain()
        {
            /*
             [
                ['A','B','C','E'],
                ['S','F','C','S'],
                ['A','D','E','E']
             ]

                "ABCCED" -> true
             */
            WordSearch ws = new WordSearch();
            rows = 3;
            cols = 4;

            char[,] board = new char[rows, cols];
            board[0, 0] = 'A'; board[0, 1] = 'B'; board[0, 2] = 'C'; board[0, 3] = 'E';
            board[1, 0] = 'S'; board[1, 1] = 'F'; board[1, 2] = 'C'; board[1, 3] = 'S';
            board[2, 0] = 'A'; board[2, 1] = 'D'; board[2, 2] = 'E'; board[2, 3] = 'E';
            
            bool x = ws.Exist(board, "SEE");
            Console.WriteLine(x);

        }
        
        static bool finalResult = true;
        public bool Exist(char[,] board, string word)
        {
            char[] arr = word.ToArray();
            List<XY> result = GetCharList(arr[0], board);
            rows = board.GetLength(0);
            cols = board.GetLength(1);
            foreach (var xy in result)
            {
                BoardChar bc = new BoardChar();
                finalResult = true;
                bc.Pos.x = xy.x;
                bc.Pos.y = xy.y;
                bc = SetNeighbors(board, bc);
                for (int i = 0; i < arr.Length; i++)
                {
                    bool cur = FindCharInBC(board, bc, arr[i]);
                    bool north = FindCharInBC(board, bc.North, arr[i]);
                    bool south = FindCharInBC(board, bc.South, arr[i]);
                    bool east = FindCharInBC(board, bc.East, arr[i]);
                    bool west = FindCharInBC(board, bc.West, arr[i]);
                    finalResult = finalResult && (cur || north  || south || east || west);
                    if (finalResult == false) break;
                    if (bc.North.IsMatched) bc = bc.North;
                    else if (bc.South.IsMatched) bc = bc.South;
                    else if (bc.East.IsMatched) bc = bc.East;
                    else if (bc.West.IsMatched) bc = bc.West;
                    bc = SetNeighbors(board, bc);
                }

                if (finalResult) return true;

            }

            return false;
        }

        public BoardChar SetNeighbors(char[,] board, BoardChar bc)
        {
            int xmin = 0;
            int ymin = 0;
            int xmax = rows - 1;
            int ymax = cols - 1;
            bc.North = new BoardChar();
            bc.South = new BoardChar();
            bc.West = new BoardChar();
            bc.East = new BoardChar();

            if (bc.Pos.x > xmin)
            {
                // North
                bc.North.Pos.x = bc.Pos.x - 1;
                bc.North.Pos.y = bc.Pos.y;

            }
            else
            {
                bc.North.Pos = null;
            }

            if (bc.Pos.x < xmax)
            {
                // South
                bc.South.Pos.x = bc.Pos.x + 1;
                bc.South.Pos.y = bc.Pos.y;
            }
            else
            {
                bc.South.Pos = null;
            }

            if (bc.Pos.y > ymin)
            {
                // West
                bc.West.Pos.x = bc.Pos.x;
                bc.West.Pos.y = bc.Pos.y - 1;
            }
            else
            {
                bc.West.Pos = null;
            }

            if (bc.Pos.y < ymax)
            { 
                // East
                bc.East.Pos.x = bc.Pos.x;
                bc.East.Pos.y = bc.Pos.y + 1;
            }
            else
            {
                bc.East.Pos = null;
            }

            return bc;
        }

        public bool FindCharInBC(char[,] board, BoardChar bc, char ch)
        {
            if (bc.IsVisited == true) return false;
            bc.IsVisited = true;
            if (bc.Pos == null) return false;
            if (board[bc.Pos.x,bc.Pos.y] == ch)
            {
                bc.IsMatched = true;
                return true;
            }

            return false;
        }


        public List<XY> GetCharList(char start, char[,] board)
        {
            List<XY> result = new List<XY>();
            for (int i = 0; i < rows; i++)
            {

                for (int j = 0; j < cols; j++)
                {
                    if (board[i,j] == start)
                    {
                        result.Add(new XY { x = i, y = j });
                    }
                }
            }

            return result;

        }


    }

}



