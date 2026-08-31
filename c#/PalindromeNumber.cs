using System;

public class gfgPalindromeNumber{
    public static bool isPalindrome(int n)
    {
        int reversed = 0;
        int N = Math.Abs(n);
        while (N > 0)
        {
            reversed = (reversed * 10) + (N % 10);
            N = N / 10;
        }
        return reversed == Math.Abs(n);
    }
}