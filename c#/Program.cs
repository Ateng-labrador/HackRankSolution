using System;
using System.Collections.Generic;
using System.Numerics;

List<List<int>> A1 = new List<List<int>>()
{
    new List<int> {1, 3, 1},
    new List<int> {1, 0, 0}
};

List<List<int>> B1 = new List<List<int>>()
{
    new List<int> {0, 0, 5},
    new List<int> {7, 5, 0}
};

int[][] A = new int[][]
{
    new int[] {1, 3, 1},
    new int[] {1, 0, 0}
};

int[][] B = new int[][]
{
   new int[] {0, 0, 5},
   new int[] {7, 5, 0}
};

List<List<int>> x = calculator_matriks.Penjumlahan(A, B);

foreach (var item in x)
{
    Console.WriteLine(string.Join(" ", item));
}

Console.WriteLine("\n");

List<List<int>> y = calculator_matriks.Pengurangan(A, B);

foreach (var item in y)
{
    Console.WriteLine(string.Join(" ", item));
}