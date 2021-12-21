using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    /// <summary>
    /// https://codefights.com/interview/xfpK5NtkLaoYEPLCT
    /// </summary>
    class ReverseInteger
    {
        public static int reverseInteger(int x)
        {
            bool isNegative = false;
            if (x < 0)
            {
                isNegative = true;
            }
            x = Math.Abs(x);
            List<int> reverse = new List<int>();
            while (x != 0)
            {
                int lastDigit = x % 10;
                reverse.Add(lastDigit);
                x = x - lastDigit;
                if (x == 0)
                { break; }
                x = x / 10;

            }
            int result = 0;
            for (int i = reverse.Count - 1; i>=0; i--)
            {
                int power = i;
                int tenToThePower = 1;
                for(int j=1; j<=power; j++)
                {
                    tenToThePower = 10 * tenToThePower;
                }
                result = result + tenToThePower * reverse[reverse.Count - (i+1)];
            }

            if (isNegative)
            {
                result = result * -1;
            }

            return result;
        }

        public static void reverseIntegerMain()
        {
            reverseInteger(12345);
        }

    }
}
