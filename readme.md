# Setup dan Jalankan Aplikasi Python

Aplikasi ini dibangun dengan menggunakan Flask untuk web framework, serta transformers dan protobuf untuk model pemrosesan teks. Berikut adalah langkah-langkah untuk menjalankan aplikasi.

## Prasyarat

- Python versi **3.10** (versi lain mungkin tidak kompatibel dengan beberapa dependensi, terutama Transformers dan Torch).
- `pip` telah terinstal.
- Koneksi internet untuk unduh model (opsional jika sudah tersedia offline).

## Langkah-langkah Instalasi

### 1. Clone Repository
Clone repository ini ke dalam mesin lokal Anda:
```
git clone <URL_REPOSITORY>
cd <NAMA_FOLDER_REPOSITORY>
```
### 2. Instalasi Dependensi
Buat instal dependensi yang diperlukan dengan perintah berikut:
```bash
pip install -r requirements.txt
```
### 3. Unduh dan Ekstrak Model
1. **Unduh model zip** dari link berikut:  
   [Download t5-mqg-base-model.zip](https://drive.google.com/file/d/19YpxcTiYDVSsYfh1r-tt5DHzG7JcVtLh/view?usp=sharing)
   
2. **Ekstrak file zip** ke dalam folder `model/`. Folder `model/` harus berada pada direktori utama aplikasi Anda. Struktur folder Anda seharusnya terlihat seperti ini:
```
   <NAMA_FOLDER_REPOSITORY>/
   ├── app.py
   ├── finetuning/
   ├── model/
   │   └── t5-mqg-base-model/
   ├── templates/
   └── requirements.txt
```
### 4. Menjalankan Aplikasi
Setelah semua langkah di atas selesai, jalankan aplikasi dengan perintah berikut:
```
python app.py
```
Aplikasi akan berjalan di http://127.0.0.1:5000 secara default. Anda dapat mengaksesnya melalui browser.


## Catatan
- Pastikan untuk memeriksa apakah file model telah diekstrak dengan benar di dalam folder `model/` sebelum menjalankan aplikasi.
- Jika Anda menemui masalah terkait model atau library yang tidak ditemukan, pastikan semua dependensi sudah terinstal dengan benar.

Selamat mencoba!
