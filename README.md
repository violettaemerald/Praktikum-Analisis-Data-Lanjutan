# Analisis Data Penjualan Toko Online  
## Laporan & Kesimpulan Tugas Modul Lanjutan Analisis Data

### Ringkasan Proyek
Telah dilakukan analisis lengkap terhadap data penjualan toko online menggunakan Python (pandas, numpy, matplotlib, seaborn). Proses mencakup data cleaning, analisis deskriptif, visualisasi, serta simulasi pemberian diskon 10% untuk melihat dampaknya terhadap pendapatan bersih.

### Key Findings & Insight Bisnis

1. **Produk Terlaris (Berdasarkan Total Pendapatan)**  
   Setelah pengelompokan dan pengurutan, produk yang paling banyak menyumbang pendapatan adalah **Laptop Gaming** dan **Smartphone Flagship**, jauh di atas produk lain seperti aksesoris atau earphone.  
   → Rekomendasi: Fokus stok dan promosi pada kedua kategori ini.

2. **Tren Pendapatan Mingguan**  
   Grafik garis menunjukkan adanya **lonjakan signifikan pada minggu ke-3 dan ke-4** (kemungkinan karena event promo atau gajian).  
   → Saran: Jadwalkan promo besar atau restock di periode yang sama setiap bulan.

3. **Dampak Pemberian Diskon 10% Secara Seragam**  
   - Total pendapatan kotor (sebelum diskon): **Rp 485.750.000**  
   - Total diskon yang diberikan: **Rp 48.575.000**  
   - Pendapatan bersih setelah diskon: **Rp 437.175.000** (turun ~10%)  
   - Namun, produk high-value (Laptop & Smartphone) tetap mendominasi pendapatan bersih (>70%).

   Insight: Diskon flat 10% untuk semua produk **kurang optimal**. Sebaiknya gunakan strategi diskon bertingkat:
   - 15–20% untuk produk low-margin / lambat laku
   - 0–5% untuk produk high-margin (Laptop, Smartphone)

4. **Kualitas Data**  
   Terdapat beberapa baris dengan nilai kosong (missing values) pada kolom Pendapatan dan Jumlah. Setelah `dropna()`, jumlah baris berkurang dari 120 ke 115.  
   → Di masa depan, sistem input penjualan perlu divalidasi agar tidak ada data hilang.


### Jawaban Evaluasi Pemahaman (Bagian F)

| No | Pertanyaan | Jawaban Singkat |
|----|------------|-----------------|
| 1  | Apa fungsi library pandas dalam analisis data? | **Pandas** digunakan untuk mengelola dan memanipulasi data berbentuk tabel (DataFrame dan Series), membaca file CSV/Excel, melakukan cleaning, filtering, grouping, dan analisis data secara efisien. |
| 2  | Apa perbedaan antara matplotlib dan seaborn? | **Matplotlib** adalah library dasar untuk membuat visualisasi (lebih low-level, banyak kontrol manual). **Seaborn** dibangun di atas matplotlib, memberikan tampilan lebih cantik secara default, lebih mudah untuk visualisasi statistik, dan integrasi baik dengan pandas. |
| 3  | Mengapa perlu melakukan data cleaning sebelum analisis? | Karena data mentah sering mengandung nilai kosong (NaN), duplikat, format salah, atau outlier. Jika tidak dibersihkan, hasil analisis dan visualisasi bisa salah, menyesatkan, atau bahkan error saat diproses. |
| 4  | Fungsi apa yang digunakan untuk menampilkan 5 data pertama dari DataFrame? | Fungsi **`df.head()`** (secara default menampilkan 5 baris pertama). Bisa juga `df.head(n)` untuk menampilkan n baris. |
| 5  | Bagaimana cara menyimpan data hasil analisis ke file CSV? | Menggunakan perintah: <br> **`df.to_csv("nama_file.csv", index=False)`** <br> Parameter `index=False` agar nomor indeks baris tidak ikut disimpan. |

### Kesimpulan Akhir
Melalui praktikum ini, saya berhasil:
- Menguasai alur end-to-end analisis data menggunakan Python
- Membuktikan bahwa visualisasi sederhana (bar chart & line chart) sudah cukup powerful untuk menemukan insight bisnis yang actionable
- Menyadari pentingnya **membersihkan data** sebelum analisis
- Memahami bahwa **diskon tidak selalu meningkatkan keuntungan** — strategi yang salah justru bisa menurunkan margin secara signifikan

Keterampilan yang diperoleh dari modul ini menjadi fondasi yang sangat kuat untuk melangkah ke tahap data analytics yang lebih advanced (forecasting, segmentasi pelanggan, machine learning, dll).


###Figure/Graphic
<img width="1000" height="500" alt="Figure_Tren" src="https://github.com/user-attachments/assets/e3a2f503-8d05-4610-8209-c6e45bb517f6" />
<img width="1000" height="500" alt="Figure_Pendapatan_Bersih" src="https://github.com/user-attachments/assets/eb2965ca-1bca-4e8d-87a6-32742d6064a2" />
<img width="800" height="500" alt="Figure_Pendapatan" src="https://github.com/user-attachments/assets/c24cb585-e6c7-44da-81d7-ff423b806974" />

