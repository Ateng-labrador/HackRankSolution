public class leetcode1572
{
    public static int DiagonalSum(int[][] mat)
    {
        int rows = mat.Length;
        int res = 0;
        for(int i = 0; i < rows; i++)
        {
            res += mat[i][i];
            res += mat[i][rows - i - 1];
        }
        if(rows % 2 != 0)
        {
            int center = rows / 2;
            res -= mat[center][center];
        }
        return res;
    }
}