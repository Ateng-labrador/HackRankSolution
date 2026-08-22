using System;
using System.Collections.Generic;

var numbers = new List<List<int>>();
for (int i = 0; i < 3; i++)
{
    var row = new List<int>();
    for (int j = 0; j < 3; j++)
    {
        row.Add(j);
    }
    numbers.Add(row);
}

foreach (var item in numbers)
{
    Console.WriteLine(string.Join(" ", item));
}
