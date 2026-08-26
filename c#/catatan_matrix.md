List<T> di C# adalah struktur data array dinamis yang ukurannya fleksibel
bisa bertambah dan berkurang secara otomatis, sangat mirip degan list di 
python namun bersifat strongly-typed (tipe datanya wajib ditentukan dan 
seragam)

**Cara Deklarasi & Inisialisasi**

```
using System.Collections.Generic;

// 1. Deklarasi list kosong
List<int> numbers = new List<int>();

// 2. Cara paling ringkas (menggunakan 'var')
var names = new List(<string()>);

// 3. Deklarasi langsung dengan isi awal
var scores = new List<int>{90, 85, 100};
```

**Membuat Matriks (2D)**
```
using System;
using System.Collections.Generic;

Matriks kosong
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
```

Perbedaan Ilist sebagai dokumen syarat/kontrak, sedangkan List adalah
barang nyata yang memenuhi syarat tersebut.

Analogi Kehidupan Nyata
    -> IList (Persyaratan): Brosur lowongan kerja: "Dicari kendaraan yang bisa berjalan, mengerem, dan belok."ini cuman daftar kemampuan, kamu tidak bisa maiki brosur ini.

    -> List (Barang Nyata): Mobil Avanza di garasimu.Ini barang fisik yang benar - benar punya mesin dan bisa kamu kendarai, rem, serta belokkan.

Implementasi:
-> Saat membuat tempat penyimpanan (Pakai List):
    Kamu butuh objek nyata di memori untuk menampung data.
    ```
    // BENAR: Bikin wadah fisik
    List<int> angka = new List<int>(); 

    // SALAH ERROR: Kamu tidak bisa bikin "brosur" jadi wadah nyata
    // IList<int> angka = new IList<int>();
    ```

->  Saat Bikin Fungsi/Method (Boleh pakai Ilist agar Fleksibel):
    Jika sebuah fungsi hanya bertugas membaca/menambah data, gunakan IList pada parameterenya agar fungsi tersebut mau menerima jenis list apa saja

    ```
    // Fungsi ini mau menerima List jenis APAPUN, asal memenuhi aturan IList
    public void CetakData(IList<int> koleksi) 
    {
        foreach (var item in koleksi) 
        {
            Console.WriteLine(item);
        }
    }
    ```




