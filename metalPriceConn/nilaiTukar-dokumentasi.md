# Konektor nilaiTukar

Konektor `nilaiTukar` memungkinkan Anda untuk mengambil dan mengimpor nilai tukar mata uang terbaru dari MetalPriceAPI. Dokumentasi ini memberikan panduan terperinci tentang cara menggunakan konektor, arti dari setiap parameter, dan parameter API.

## Persyaratan

- **API Key**: Anda memerlukan API key dari MetalPriceAPI untuk mengakses data mereka. Anda dapat memperoleh API key dengan mendaftar di [MetalPriceAPI website](https://metalpriceapi.com/).

## Instalasi

Untuk menginstal konektor `nilaiTukar`, Anda perlu memiliki paket Python berikut:
- `requests`
- `datetime`

Anda dapat menginstal paket yang diperlukan menggunakan pip:

```bash
pip install requests
```

## Konfigurasi

### Konfigurasi Koneksi (`conn_config`)

| Parameter | Wajib | Deskripsi                                    | Tipe Input |
|-----------|-------|----------------------------------------------|------------|
| api_key   | Ya    | API Key untuk mengakses MetalPriceAPI        | String     |

### Konfigurasi Impor (`import_config`)

| Parameter  | Wajib | Deskripsi                                                                                  | Tipe Input |
|------------|-------|--------------------------------------------------------------------------------------------|------------|
| mataUang   | Ya    | Daftar kode mata uang yang dipisahkan dengan koma, misalnya: `IDR,EUR,XAU,XAG`.             | String     |
| base       | Ya    | Kode mata uang dasar, misalnya: `XAU` (Emas) atau `EUR`.                                    | String     |

## Penggunaan

### cara menghubungkan

anda perlu melakukan pengambilan api di website [MetalPriceAPI website](https://metalpriceapi.com/)


### Mengimpor Data

Untuk mengimpor data, Anda perlu menentukan parameter untuk impor. Berikut adalah contoh cara mengimpor data:

```python
import_params = {
    'mataUang': 'IDR,EUR,XAU,XAG',
    'base': 'USD'
}

conn_params = {
    'api_key': 'YOUR_API_KEY_HERE'
}

dest_table = 'your_destination_table'

nilaiTukar.import_(import_params, conn_params, dest_table)
```

### Parameter

- **mataUang**: Daftar kode mata uang yang dipisahkan dengan koma untuk dikonversi. Periksa kode mata uang yang tersedia di [Halaman Mata Uang MetalPriceAPI](https://metalpriceapi.com/currencies).
- **base**: Kode mata uang dasar untuk konversi. Periksa kode mata uang yang tersedia di [Halaman Mata Uang MetalPriceAPI](https://metalpriceapi.com/currencies).

### Parameter API

Konektor ini menggunakan MetalPriceAPI untuk mengambil nilai tukar mata uang terbaru berdasarkan parameter yang ditentukan. Parameter API berikut digunakan dalam permintaan:

- **api_key**: Kunci API Anda dari MetalPriceAPI.
- **base**: Mata uang dasar untuk konversi.
- **currencies**: Daftar mata uang tujuan yang dipisahkan dengan koma.

### Contoh Respons

Konektor mengambil data dalam format berikut:

```json
[
    {
        "base": "USD",
        "currency": "IDR",
        "rate": 14210.5,
        "timestamp": "2023-06-23T12:34:56.789Z"
    },
    {
        "base": "USD",
        "currency": "EUR",
        "rate": 0.8435,
        "timestamp": "2023-06-23T12:34:56.789Z"
    },
    ...
]
```

### Memasukkan Data

Data yang diambil akan dimasukkan ke dalam tabel database yang ditentukan. Skema tabel harus sesuai dengan format data yang diambil.

## Penanganan Kesalahan

Jika permintaan API gagal, `APIError` akan muncul dengan kode status dan pesan kesalahan yang sesuai. Jika struktur respons tidak valid, `APIError` juga akan muncul.

## Catatan

- Pastikan API key Anda memiliki izin yang diperlukan untuk mengakses MetalPriceAPI.
- Konektor akan memperbarui nilai tukar setiap kali dipanggil, mengambil nilai tukar terbaru.
