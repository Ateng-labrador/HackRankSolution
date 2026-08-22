using System;
using System.Collections.Generic;

public class calculator_matriks
{
    public static int[,] penjumlahan(int[,] A, int[,] B)
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

    public static int[,] pengurangan(int[,] A, int[,] B)
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

}