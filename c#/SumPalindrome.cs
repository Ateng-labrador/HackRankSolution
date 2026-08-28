using System.ComponentModel;

public class SumPalindrome
{
    public static bool Palindrome(int n)
    {
        int r = 0;
        int N = n;
        while (N > 0)
        {
            r = (r * 10) + (N % 10);
            N = N / 10;
        }
        return n == r;
    }

    public static int reverse(int n)
    {
        int r = 0;
        int N = n;
        while (N > 0)
        {
            r = (r * 10) + (N % 10);
            N = N / 10;
        }
        return r;
    }

    public static int isSumPalindrome(int n)
    {
        if (SumPalindrome.Palindrome(n))
        {
            return n;
        }

        int ite = 0;
        int N = n;
        while (ite < 5)
        {
            int res = N + SumPalindrome.reverse(N);
            if (SumPalindrome.Palindrome(res))
            {
                return res;
            }
            else
            {
                ite += 1;
                N = res;
            }
        }
        return -1;
    }
}