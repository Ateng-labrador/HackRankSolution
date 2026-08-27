using System.Diagnostics;

public class leetcode2319
{
    public static bool CheckXMatrix(int[][] grid)
    {
        for(int i = 0; i < grid.Length; i++)
        {
            for(int j = 0; j < grid[0].Length; j++)
            {
                // Diagonal
                if(i == j || i + j == grid.Length - 1)
                {
                    if(grid[i][j] == 0)
                    {
                        return false;
                    }
                    
                }
                else
                {
                    if(grid[i][j] != 0)
                    {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}