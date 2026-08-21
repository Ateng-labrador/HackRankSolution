using System.Linq;
using System.Collections.Generic;

public class Solution
{
    public int CountPairs(IList<int> nums, int target)
    {
        nums = nums.OrderBy(n => n).ToList();
        int L = 0;
        int R = nums.Count - 1;
        int res = 0;
        while (L < R)
        {
            if (nums[L] + nums[R] < target)
            {
                res += (R - L);
                L += 1;
            }
            else
            {
                R -= 1;
            }
        }
        return res;
    }

    public int CountPairs1(IList<int> nums, int target)
    {
        int res = 0;
        for (int i = 0; i < nums.Count - 1; i++)
        {
            for(int j = i + 1; j < nums.Count; j++)
            {
                if(nums[i] + nums[j] < target)
                {
                    res++;
                }
            }
        }
        return res;
    }
}
