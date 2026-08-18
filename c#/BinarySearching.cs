public class BinarySearching
{
    /// <summary>
    /// Algoritma ini bertujuan untuk mencari sebuah nilai pada array
    /// </summary>
    public static int binarysearch(int[] A, int t)
    {
        int L = 0;
        int R = A.Length - 1;
        while (L <= R){
            int m = (L + R) / 2;
            if (A[m] > t)
            {
                R = m - 1;
            }
            else if(A[m] < t)
            {
                L = m + 1;
            }
            else
            {
                return m;
            }
        }
        return -1;
    }
    /// <summary>
    /// Sama mencari sebuah nilai pada sebuah array tapi ini versi alternatifnya
    /// </summary>
    public static int binary_search_alternative(int[] A, int t)
    {
        int L = 0;
        int R = A.Length - 1;
        while (L != R)
        {
            int m = (R + L) / 2;
            if (A[m] > t)
            {
                R = m - 1;
            }
            else
            {
                L = m;
            }
        }
        if (A[L] == t)
        {
            return L;
        }
        return -1;
    }
    /// <summary>
    /// Binary Search tapi memastikan posisi paling kiri
    /// </summary>
    public static int binary_search_leftmost(int[] A, int t)
    {
        int L = 0;
        int R = A.Length;
        while(L < R)
        {
            int m = (R - L) / 2;
            if(A[m] < t)
            {
                L = m + 1;
            }
            else
            {
                R = m;
            }
        }
        return L;
    }
    /// <summary>
    /// Binary Search tapi memastikan posisi paling kanan
    /// </summary>
    public static int binary_search_rightmost(int[] A, int t)
    {
        int L = 0;
        int R = A.Length;
        while (L < R)
        {
            int m = (R - L) / 2;
            if (A[m] > t)
            {
                R = m;
            }
            else
            {
                L = m + 1;
            }
        }
        return R - 1;
    }
}