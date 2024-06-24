# ViralContentAPI Connector

## Pendahuluan
`ScrapKontenViral` adalah custom connector api yang digunakan untuk mengambil informasi video viral sebanyak 50 baris dan bisa memilih berdasarkan kategori dan negara apa yang ingin dilakukan analisis atau scrap data.


## Persyaratan

### Mendapatkan API Key
1. Buka [Google Cloud Console](https://console.cloud.google.com/) atau akses [video tutorial](https://youtu.be/LLAZUTbc97I?si=OJUOOKZS03VCRYYG).
2. Buat proyek baru atau pilih proyek yang sudah ada.
3. Aktifkan YouTube Data API v3 di library API.
4. Buat kredensial untuk API Key dan simpan API key yang dihasilkan.

## Instalasi

Untuk menginstal connector `ViralContentAPI`, Anda perlu memiliki paket Python berikut:
- `requests`
- `datetime`

Anda dapat menginstal paket yang diperlukan menggunakan pip:

```bash
pip install requests
```

## Konfigurasi

### Konfigurasi Koneksi (`conn_config`)

| Parameter | Wajib   | Deskripsi                           | Tipe Input |
|-----------|---------|-------------------------------------|------------|
| api_key   | Ya      | API Key untuk mengakses data YouTube.| String     |

### Konfigurasi Impor (`import_config`)

## Konfigurasi Import
Berikut adalah konfigurasi yang diperlukan untuk memilih jenis kontent dan negara apa yang ingin di scrap menggunakan GUI dropDown, anda bisa menambahkan sesuai kebutuhan anda di key negara. kedua parameter dibawah ini adalah mengharuskan pengguna mengisikan field tersebut.


| Parameter    | Wajib   | Deskripsi                                      | Tipe Input | Opsi                                                                                         |
|--------------|---------|------------------------------------------------|------------|----------------------------------------------------------------------------------------------|
| kategori     | Ya      | Kategori konten yang ingin diambil.            | Dropdown   | `Video`                                                                                      |
| negara       | Ya      | Negara yang ingin dianalisis.                  | Dropdown   | `Indonesia (ID)`, `Malaysia (MY)`, `Philippines (PH)`, `Singapore (SG)`, `USA (US)`          |
| maxResults   | Tidak   | Jumlah maksimum hasil yang ingin diambil (1-50).| Nomor      | Default adalah 50                                                                            |



## Penggunaan

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

### import data

import data memerlukan parameter sebagai berikut:

```python
import_params = {
    'negara': 'US',
    'maxResults': 50
}

conn_params = {
    'api_key': 'YOUR_API_KEY_HERE'
}

dest_table = 'your_destination_table'

ViralContentAPI.import_(import_params, conn_params, dest_table)
```

### Parameter

- **kategori**: Kategori konten yang ingin diambil. Saat ini, hanya 'video' yang didukung.
- **negara**: Negara yang ingin dianalisis. Anda bisa memilih dari opsi berikut:
  - `Indonesia (ID)`
  - `Malaysia (MY)`
  - `Philippines (PH)`
  - `Singapore (SG)`
  - `USA (US)`
- **maxResults**: Jumlah maksimum baris yang ingin diambil. nilai dalam bentuk default adalah 50.

### Parameter API

Connector menggunakan YouTube Data API v3 untuk mengambil video paling populer berdasarkan parameter yang ditentukan. Parameter API berikut digunakan dalam permintaan:

- **part**: Menentukan bagian sumber daya yang akan disertakan dalam respons API. Connector mengambil `snippet`, `contentDetails`, dan `statistics`.
- **chart**: Menentukan chart yang akan diambil. Connector menggunakan `mostPopular` untuk mendapatkan video paling populer.
- **regionCode**: Menentukan negara untuk mengambil chart.
- **maxResults**: Menentukan jumlah maksimum item yang harus dikembalikan dalam set hasil.
- **key**: API key Anda dari YouTube.

### Contoh Respons

Connector mengambil data dalam format berikut:

```json
[
    {
        "video_id": "video_id_here",
        "title": "Judul Video",
        "description": "Deskripsi Video",
        "published_at": "2023-01-01T00:00:00Z",
        "view_count": "123456",
        "like_count": "1234",
        "comment_count": "123",
        "timestamp": "2023-06-23T12:34:56.789Z",
        "jenis_konten": "video"
    },
    ...
]
```

### Menyisipkan Data

Data yang diambil dimasukkan ke dalam tabel database yang ditentukan. Skema tabel harus sesuai dengan format data yang diambil.

## Penanganan Kesalahan

Jika permintaan API gagal, `APIError` akan muncul dengan kode status dan pesan kesalahan yang sesuai.
