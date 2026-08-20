public class leetcode2824
{
    public static int solution(int[] arr, int t)
    {
        Array.Sort(arr);
        int L = 0;
        int R = arr.Length - 1;
        int res = 0;

        while(L < R)
        {
            if(arr[L] + arr[R] < t)
            {
                res += (R - L);
                L++;
            }
            else
            {
                R--;
            }
        }
        return res;
    }
}
