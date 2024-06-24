# ScrapKontenViral Documentation

## Pendahuluan
`ScrapKontenViral` adalah custom connector api yang digunakan untuk mengambil informasi video viral sebanyak 50 baris dan bisa memilih berdasarkan kategori dan negara apa yang ingin dilakukan analisis atau scrap data melalui [keloola exchange](https://bigdata.keloola.com).

## API Key
Untuk menggunakan connector ini, Anda memerlukan API key dari YouTube. API key ini diperlukan untuk otentikasi dan otorisasi akses ke YouTube Data API.

### Mendapatkan API Key
1. Buka [Google Cloud Console](https://console.cloud.google.com/) atau akses [video tutorial](https://youtu.be/LLAZUTbc97I?si=OJUOOKZS03VCRYYG).
2. Buat proyek baru atau pilih proyek yang sudah ada.
3. Aktifkan YouTube Data API v3 di library API.
4. Buat kredensial untuk API Key dan simpan API key yang dihasilkan.

## Konfigurasi Koneksi
Berikut adalah konfigurasi yang diperlukan untuk menghubungkan ke API YouTube:

### Parameter Koneksi
- **api_key** (wajib): API Key untuk mengakses YouTube.
  - **Judul**: API Key
  - **Deskripsi**: API Key untuk mengakses YouTube

## Konfigurasi Import
Berikut adalah konfigurasi yang diperlukan untuk memilih jenis kontent dan negara apa yang ingin di scrap menggunakan GUI dropDown, anda bisa menambahkan sesuai kebutuhan anda di key negara. kedua parameter dibawah ini adalah mengharuskan pengguna mengisikan field tersebut.

### Parameter Import
- **kategori** (wajib): Kategori konten yang ingin diambil.
  - **Judul**: Kategori Konten
  - **Deskripsi**: Kategori konten yang ingin diambil
  - **Tipe Input**: Dropdown
  - **Opsi**:
    - **Data**: 
      - **Label**: Video, **Value**: video
    - **Tampilan**: Label
    - **Nilai**: Value
- **negara** (wajib): Negara yang ingin dianalisa.
  - **Judul**: Negara yang ingin dianalisa
  - **Deskripsi**: Pilih negara
  - **Tipe Input**: Dropdown
  - **Opsi**:
    - **Data**: 
      - **Label**: Indonesia, **Value**: ID
      - **Label**: Malaysia, **Value**: MY
      - **Label**: Philippines, **Value**: PH
      - **Label**: Singapore, **Value**: SG
      - **Label**: USA, **Value**: US
    - **Tampilan**: Label
    - **Nilai**: Value

## Fungsi Kelas

### `connect(cls, conn_params: dict, **kwargs)`
Fungsi ini digunakan untuk memvalidasi dan menghubungkan menggunakan API key yang diberikan.

- **Parameter**:
  - `conn_params` (dict): Parameter koneksi yang berisi API key.
  - `kwargs`: Argumen tambahan.


### `import_(cls, import_params: dict, conn_params: dict, dest_table: str, **kwargs)`
Fungsi ini digunakan untuk mengambil data dari YouTube berdasarkan parameter yang diberikan dan menyimpannya ke dalam tabel database.

- **Parameter**:
  - `import_params` (dict): Parameter import digunakan untuk menangkap key dari variable import_config.
  - `conn_params` (dict): Parameter koneksi yang berisi API key.
  - `dest_table` (str): Nama tabel tujuan di database.
  - `kwargs`: Argumen tambahan.

- **Contoh Penggunaan**:
  ```python
  import_params = {
      'kategori': 'video',
      'negara': 'ID'
  }
  conn_params = {
      'api_key': 'YOUR_API_KEY'
  }
  ViralContentAPI.import_(import_params, conn_params, 'youtube_videos')
  ```

## Struktur Data Hasil
Data hasil dari import akan memiliki struktur sebagai berikut:

- **video_id**: ID video YouTube
- **title**: Judul video
- **description**: Deskripsi video
- **published_at**: Tanggal publikasi video
- **view_count**: Jumlah penayangan
- **like_count**: Jumlah suka
- **comment_count**: Jumlah komentar
- **timestamp**: Timestamp saat data diambil
