import requests
from utils.connector.base import BaseConnector, db, current_ds, APIError
from datetime import datetime

class nilaiTukar(BaseConnector):
    conn_config = {
        'api_key': {
            'required': True,
            'title': 'API Harga Emas',
            'description': 'Masukkan API key dari metalpriceapi.com di sini'
        }
    }

    import_config = {
        'mataUang': {
            'required': True,
            'title': 'Daftar Mata Uang',
            'description': 'Ketik kode mata uang, misal: IDR,EUR,XAU,XAG atau cek https://metalpriceapi.com/currencies'
        },
        'base': {
            'required': True,
            'title': 'base nilai tukar',
            'description': 'ketik 1 kode mata uang utama, misal: XAU(Emas) atau EUR atau cek https://metalpriceapi.com/currencies'
        }
    }

    @classmethod
    def connect(cls, conn_params: dict, **kwargs):
        api_key = conn_params.get('api_key')
        if not api_key:
            raise ConnectionError('API Key is required')

    @classmethod
    def import_(cls, import_params: dict, conn_params: dict, dest_table: str, **kwargs):
        api_key = conn_params.get('api_key')
        mata_uang_list = [x.strip() for x in import_params.get('mataUang', '').split(',')]
        base = import_params.get('base')
        
        if not mata_uang_list and not base:
            raise ValueError("Mata uang tidak boleh kosong dan base tidak boleh kosong")
        
        mata_uang_str = ','.join(mata_uang_list)
        
        url = "https://api.metalpriceapi.com/v1/latest"
        params = {
            'api_key': api_key,
            'base': base,
            'currencies': mata_uang_str
        }
        
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise APIError(f"Request failed with status code {response.status_code}")
        
        res = response.json()
        if 'rates' not in res:
            raise APIError("Invalid response structure")
        
        results = []
        for currency, rate in res['rates'].items():
            temp = {
                'base': base,
                'currency': currency,
                'rate': rate,
                'timestamp': datetime.now()
            }
            results.append(temp)
        
        db.insert_rows_to_db(results, dest_table, current_ds.engine, if_exists='replace')

