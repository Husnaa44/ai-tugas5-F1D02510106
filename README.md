# Sistem Pakar Pemilahan Sampah Rumah Tangga

## 1. Identitass
- **Nama:** Asmaul Husnah
- **NIM:** F1D02510106

## 2. Topik dan Cara Menjalankan
- **Topik:** Klasifikasi Pemilahan Sampah Rumah Tangga (Organik, Anorganik, B3 Rumah Tangga, dan Residu).
- **Bahasa:** Python 3 (menggunakan modul bawaan `json` dan `os`).
- **Cara Menjalankan:**
  1. Buka terminal di folder repository ini.
  2. Jalankan perintah:
     ```bash
     python main.py
     ```
  3. Jawab pertanyaan ciri sampah dengan `y` (ya) atau `t` (tidak).

## 3. Daftar Sumber dan Tabel Aturan

### Sumber Pengetahuan
- **S1:** Peraturan Menteri LHK Nomor 14 Tahun 2021 tentang Pengelolaan Sampah pada Bank Sampah, Kementerian Lingkungan Hidup dan Kehutanan RI, https://peraturan.bpk.go.id/Details/185741/permen-lhk-no-14-tahun-2021, diakses 13 Nov 2026.
- **S2:** Pilah Sampah Organik, Anorganik, dan Residu, Dinas PUPRKIM Provinsi Bali, https://dispuprkim.baliprov.go.id/posterpilahsampah/, diakses 13 Nov 2026.

### Tabel Aturan (`kb_sampah.json`)
| Aturan | IF | Mode | THEN | Sumber |
| :--- | :--- | :---: | :--- | :---: |
| **R1** | `sisa makanan atau sayuran` OR `daun kering atau ranting` | `atau` | `Sampah Organik (Wadah Hijau - Bisa Dikomposkan)` | S2 |
| **R2** | `botol atau kemasan plastik bersih` OR `kertas kardus atau kaleng` | `atau` | `Sampah Anorganik (Wadah Kuning - Setor Bank Sampah)` | S1 |
| **R3** | `baterai bekas atau lampu neon` OR `kaleng aerosol atau pembersih kimia` | `atau` | `Sampah B3 Rumah Tangga (Wadah Merah - Penanganan Khusus)` | S1 |
| **R4** | `popok sekali pakai atau pembalut` OR `tisu bekas atau puntung rokok` | `atau` | `Sampah Residu (Wadah Abu-abu - Angkut ke TPA)` | S2 |

## 4. Metode yang Dipilih
- **Metode:** Forward Chaining (FC)
- **Alasan:** Pemilahan sampah dimulai dari ciri fisik sampah yang diamati langsung oleh pengguna (fakta awal), lalu program menelusuri aturan secara bertahap sampai menemukan kategori wadah sampah yang sesuai. Metode ini juga bisa mendeteksi lebih dari satu kategori jika sampah tercampur.

## 5. Kasus Uji dan Screenshot

| # | Jawaban `y` (Ya) | Kesimpulan yang Diharapkan |
| :---: | :--- | :--- |
| 1 | `sisa makanan atau sayuran` | `Sampah Organik (Wadah Hijau - Bisa Dikomposkan)` |
| 2 | `botol atau kemasan plastik bersih` | `Sampah Anorganik (Wadah Kuning - Setor Bank Sampah)` |
| 3 | `baterai bekas atau lampu neon`, `popok sekali pakai atau pembalut` | `Sampah B3 Rumah Tangga (Wadah Merah - Penanganan Khusus)`; `Sampah Residu (Wadah Abu-abu - Angkut ke TPA)` |

### Screenshot Program
1. **Kasus 1 (Sampah Organik):**
   ![Kasus 1](screenshot/sampah_organik.png)

2. **Kasus 2 (Sampah Anorganik):**
   ![Kasus 2](screenshot/sampah_anorganikk.png)

3. **Kasus 3 (Multi Kesimpulan B3 dan Residu):**
   ![Kasus 3](screenshot/sampahB3_dan_residu.png)

## 6. Batas Keberlakuan
Aturan diambil dari regulasi Permen LHK No. 14 Tahun 2021 dan poster edukasi Dinas PUPRKIM Provinsi Bali. Sistem ini hanya untuk membantu pemilahan awal sampah skala rumah tangga (organik, anorganik, B3, dan residu), bukan keputusan akhir untuk limbah industri atau medis.

## 7. Penggunaan Alat Bantu AI
Menggunakan AI untuk membantu mencari referensi dan ide terkait topik sistem pakar sampah rumah tangga, memeriksa kesesuaian materi, memberikan saran perbaikan isi, serta mengecek kembali kelengkapan format README dan tampilan output program.
