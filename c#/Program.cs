using System;
using System.Collections.Generic;

IList<int> numbers = new List<int> {1, 2, 3};
for (int i = 1; i < 10; i++)
{
    numbers.Add(i);
}

Console.WriteLine(string.Join(", ",numbers));
