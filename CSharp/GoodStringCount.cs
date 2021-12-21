
namespace Test
{
    /// <summary>
    /// https://codefights.com/interview/vzzkv5NHFMELWSwAS
    /// </summary>
    class GoodStringCount
    {
        public static double goodStringsCount(int len)
        {
            if (len == 1) return 0;

            if (len >= 10) return 0;

            double count = 0;
            int x = 0;
            switch(len)
            {
                case 2:
                    x = 25;
                    break;
                case 3:
                    x = 25;
                    break;
                case 4:
                    x = 24;
                    break;
                case 5:
                    x = 23;
                    break;
            }
            for (int i =x; i>=1; i --)
            {
                double res = (i - 1) * i;
                count += res;
            }
            return (count * (len - 1));
        }

        public static void goodStringsCountMain()
        {
            goodStringsCount(4);

        }
    }
}
