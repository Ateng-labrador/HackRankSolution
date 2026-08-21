using System;
using System.Collections.Generic;

// IList<int> numbers = new List<int> {1, 2, 3};
// for (int i = 1; i < 10; i++)
// {
//     numbers.Add(i);
// }

// Console.WriteLine(string.Join(", ",numbers));

IList<int> nums = new List<int> {-1,1,2,3,1};
int target = 2;
Solution mesin_hitung = new Solution();
int hasil = mesin_hitung.CountPairs1(nums, target);
Console.WriteLine(hasil);
