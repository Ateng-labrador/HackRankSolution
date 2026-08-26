using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;

public class calculator_matriks
{
    public static int[,] penjumlahan1(int[,] A, int[,] B)
    {
        int rows = A.GetLength(0);
        int cols = A.GetLength(1);
        int[,] res = new int[rows, cols];

        for(int i = 0; i<rows; i++)
        {
            for(int j = 0; j<cols; j++)
            {
                res[i, j] = A[i, j] + B[i, j];
            }
        }
        return res;
    }

    public static int[,] pengurangan2(int[,] A, int[,] B)
    {
        int rows = A.GetLength(0);
        int colm = A.GetLength(1);
        int[,] res = new int[rows, colm];
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < colm; j++)
            {
                res[i, j] = A[i, j] - B[i, j];
            }
        }
        return res;
    }

    public static List<List<int>> Penjumlahan(int[][] A, int[][] B)
    {
        int rows = A.Length;
        int colm = A[0].Length;

        List<List<int>> res = [];

        for (int i = 0; i < rows; i++)
        {
            List<int> row = [];
            for (int j = 0; j < colm ; j++)
            {
                int x = A[i][j] + B[i][j];
                row.Add(x);
            }
            res.Add(row);
        }
        return res;
    }

    public static List<List<int>> Pengurangan(int[][] A,int[][] B)
    {
        int rows = A.Length;
        int colm = A[0].Length;

        List<List<int>> res = [];
        for(int i = 0; i < rows; i++)
        {
            List<int> row = [];
            for(int j = 0; j < colm; j++)
            {
                int x = A[i][j] - B[i][j];
                row.Add(x);
            }
            res.Add(row);
        }
        return res;
    }

    public static int[,] Perkalian(int[][] A, int[][] B)
    {
        int rows = A.Length;
        int colm = B[0].Length;
        int[,] res = new int[rows, colm];
        
        for(int i = 0; i < rows; i++)
        {
            for(int j = 0; j < colm; j++)
            {
                for(int k = 0; k < B.Length ; k++)
                {
                    res[i, j] += A[i][k] * B[k][j];
                }
            }
        }
        return res;
    }

    public static int[][] Perkalian_skalar(int[][] A, int B)
    {
        int rows = A.Length;
        int colm = A[0].Length;
        for(int i = 0; i < rows; i++)
        {
            for(int j = 0;j<colm; j++)
            {
                A[i][j] *=  B;
            }
        }
        return A;
    }

}