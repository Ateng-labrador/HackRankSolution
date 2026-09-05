using System;
using System.Collections.Generic;
using System.Security.Cryptography.X509Certificates;

List<List<int>> x = leetcode119.getRow(5);
foreach (var item in x)
{
  Console.WriteLine(string.Join(", ", item));
}


