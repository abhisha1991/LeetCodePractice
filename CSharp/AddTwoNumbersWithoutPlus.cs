// https://leetcode.com/problems/sum-of-two-integers/description/
// https://leetcode.com/problems/sum-of-two-integers/discuss/84290
public class GetSumSolution {
    public int GetSum(int a, int b) {
        if (a == 0)
            return b;
        if (b == 0)
            return a;
        if (a == -b)
            return 0;
        bool flag = false;
        if (a > 0 && b < 0)
        {
            flag = true;
        }
        if (a < 0 && b > 0)
        {
            flag = true;
            int temp = a;
            a = b;
            b = temp;
        }
        Console.WriteLine("A is " + a);
        Console.WriteLine("B is " + b);
        Console.WriteLine("Flag is " + flag);
        while (b != 0) {
            int c = a & b;
            if (flag)
            {
                c = (~a + 1) & b;
            }
		a = a ^ b;
		b = c << 1;
	}
	
	return a;
    }
   
}