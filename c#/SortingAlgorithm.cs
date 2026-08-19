/// <summary>
/// Sorting Algorithm
/// 
/// Sorting Algorithm digunakan untuk mengurutkan sebuah array
/// </summary>
public class SortingAlgorithm
{
    public static void BubbleSort(int[] A)
    {
        int n = A.Length;
        bool swapped;
        do
        {
            swapped = false;
            for(int i = 1;i < n; i++)
            {
                if(A[i - 1] > A[i])
                {
                    (A[i - 1], A[i]) = (A[i], A[i - 1]);
                    swapped = true;
                }
            }
        } while (swapped);
    }

    public static void BubbleSortOptimizi(int[] A)
    {
        int n = A.Length;
        bool swapped;
        do
        {
            swapped = false;
            for(int i = 1;i < n; i++)
            {
                if(A[i - 1] > A[i])
                {
                    (A[i - 1], A[i]) = (A[i], A[i - 1]);
                    swapped = true;
                }
            }
            n -= 1;
        } while (swapped);
    }

    public static void BubbleSortSwapp(int[] A)
    {
        int n = A.Length;
        while (n > 1)
        {
            int newn = 0;
            for (int i = 1; i < n - 1; i++)
            {
                if (A[i - 1] > A[i])
                {
                    (A[i - 1], A[i]) = (A[i], A[i - 1]);
                    newn = i;
                }
            }
            n = newn; 
        }
        Console.WriteLine(A);
    }

    public static void mergeSwap()
    {
        
    }
}
