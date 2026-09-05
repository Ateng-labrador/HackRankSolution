using System.Collections.Generic;
using System.Text.RegularExpressions;
using System.Linq;

public class leetcode119
{
    public static List<List<int>> getRow(int rowIndex)
    {
        List<List<int>> res = [];
        for(int i = 0; i < rowIndex; i++)
        {
            List<int> row = Enumerable.Repeat(1, i + 1).ToList();
            for(int j = 1; j < i; j++)
            {
                row[j] = res[i - 1][j - 1] + res[i - 1][j];
            }
            res.Add(row);
        }
        return res;
    }
}