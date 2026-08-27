using System;
using System.Collections.Generic;

int[][] mat =
{
  new int[] {2, 0, 0, 1},
  new int[] {0, 3, 1, 0},
  new int[] {0, 5, 2, 0},
  new int[] {4, 0, 0, 2}
};

int[][] mat1 =
{
    new int[] {5, 7, 0},
    new int[] {0, 3, 1},
    new int[] {0, 5, 0}
};

bool x = leetcode2319.CheckXMatrix(mat);
Console.Write(x);