public class leetcode1260
{
    public static IList<IList<int>> ShiftGrid_(int[][] grid)
    {
        int m = grid.Length;
        int n = grid[0].Length;

        var res = new List<IList<int>>();
        for(int i = 0; i<m; i++)
        {
            for(int j = 0; j<n; j++)
            {
                if(j < grid.GetLength(1) - 1)
                {
                    res[i][j + 1] = grid[i][j];
                }
                else if(i <grid.GetLength(0) - 1)
                {
                    res[i + 1][0] = grid[i][j];
                }
                else
                {
                    res[0][0] = grid[i][j];
                }
            }
        }
        return res;
    }

    public static IList<IList<int>> ShiftGrid(int[][] grid, int k)
    {
        var grid = new List<IList<int>>();
        for(int i = 0; i < k; i++)
        {
            grid = leetcode1260.ShiftGrid_(grid);
        }
        return res;
    }
}