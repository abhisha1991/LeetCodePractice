using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    /// <summary>
    /// https://codefights.com/interview/BgjZ2duKaYrrjsGcK
	/// Not efficient, see python solution instead
    /// </summary>
    class RotateImage
    {
        private static int[][] rotateImage(int[][] a)
        {
            if (a.Length == 0) return new int[0][];

            int temp;
            // replace i,j th element with j,i th element
            for (int i = 0; i < a.Length; i++)
            {
                int k = 0;
                for (int j = a[i].Length -1; k < a[i].Length - i; j--, k++)
                {
                    temp = a[i][j];
                    a[i][j] = a[j][i];
                    a[j][i] = temp;
                }
            }

            // Reverse row wise
            for (int i = 0; i < a.Length; i++)
            {
                a[i] = a[i].Reverse().ToArray();
            }

            /*
             rotateImage(a) =
                [[7, 4, 1],
                [8, 5, 2],
                [9, 6, 3]]

             */
            return a;
        }

        public static void rotateImageMain()
        {
            var x = new int[3][];
            x[0] = new int[3] { 1, 2, 3 }; // 1 4 7 --> 7 4 1
            x[1] = new int[3] { 4, 5, 6 }; // 2 5 8 --> 8 5 2 
            x[2] = new int[3] { 7, 8, 9 }; // 3 6 9 --> 9 6 3
            rotateImage(x);
        }
    }
}
