using System;
using System.Collections.Generic;

namespace Test
{
    class VisiblePoints
    {
        public static int number = 11;
        public static int actualNumber = 0;
        public static double tolerance = .0001;

        public static int visiblePoints(int[][] points)
        {
            Console.WriteLine(points.Length);
            double multiplier = 180 / Math.PI;
            double tan1 = 2f / 3f;
            double tan2 = 1f / 5f;
            double line1Angle = Math.Atan(tan1) * multiplier;
            double line2Angle = 90 - (Math.Atan(tan2) * multiplier);
            int countVisible = 0;
            for (int i = 0; i < actualNumber; i++)
            {
                double x = points[i][0];
                double y = points[i][1];
                if (x < 0 || y < 0)
                {
                    continue;
                }
                double calcYMin = Math.Tan(line1Angle / multiplier) * x;
                double calcYMax = Math.Tan(line2Angle / multiplier) * x;
                if (y >= calcYMin && y <= calcYMax)
                {
                    Console.WriteLine(x.ToString() + "," + y.ToString());
                    countVisible++;
                }

                if (Math.Abs(y - calcYMin) <= tolerance || Math.Abs(y - calcYMax) <= tolerance)
                {
                    countVisible++;
                }
            }
            return countVisible;
        }

        public static void visiblePointsMain()
        {

            int[][] points = new int[number][];

            List<int> x = new List<int> { 3, 0 }; // {1,3,3,3,1,2,1,-1,-1,-2,-4};
            List<int> y = new List<int> { -2, 2 }; // {1,1,2,3,3,5,5,-1,-2,-3,-4 };
            actualNumber = Math.Min(x.Count, y.Count);
            actualNumber = Math.Min(actualNumber, number);

            for (int i = 0; i < actualNumber; i++)
            {
                points[i] = new int[2];
                points[i][0] = x[i];
                points[i][1] = y[i];
            }

            visiblePoints(points);
        }
    }
}
