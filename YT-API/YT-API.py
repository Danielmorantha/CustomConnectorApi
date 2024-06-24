import requests
from utils.connector.base import BaseConnector, db, current_ds, APIError
from datetime import datetime

#Daniel Morantha

# API key
# AIzaSyA4UjevLqLWIROno5_e2kYgBGLDNvPzkB0

class ScrapKontenViral(BaseConnector):
    conn_config = {
        'api_key': {
            'required': True,
            'title': 'API Key',
            'description': 'API Key untuk mengakses YouTube'
        }
    }

    import_config = {
        'kategori': 
        {
            'required': True,
            'title': 'Kategori Konten',
            'description': 'Kategori konten yang ingin diambil',
            'input_type': 'dropdown',
            'options': 
            {
                'data': [
                    {'label': 'Video', 'value': 'video'}
                ],
                'display': 'label',
                'value': 'value'
            }
        },
        'negara': 
        {
            'required': True,
            'title': 'Negara yang ingin di analisa',
            'description': 'pilih negara',
            'input_type': 'dropdown',
            'options': 
            {
                'data': 
                [
                    {'label': 'Indonesia', 'value': 'ID'},
                    {'label': 'Malaysia', 'value': 'MY'},
                    {'label': 'Philippines', 'value': 'PH'},
                    {'label': 'Singapore', 'value': 'SG'},
                    {'label': 'USA', 'value': 'US'}
                ],
                'display': 'label',
                'value': 'value'
            }
        }
    }

    @classmethod
    def connect(cls, conn_params: dict, **kwargs):
        api_key = conn_params.get('api_key')
        if not api_key:
            raise ValueError("API Key tidak boleh kosong")

    @classmethod
    def import_(cls, import_params: dict, conn_params: dict, dest_table: str, **kwargs):
        api_key = conn_params.get('api_key')
        kategori = import_params.get('kategori', 'video')
        negara = import_params.get('negara')

        url = "https://www.googleapis.com/youtube/v3/videos"
        params = {
            'part': 'snippet,contentDetails,statistics',
            'chart': 'mostPopular',
            'regionCode': negara,
            'maxResults': 50,
            'key': api_key
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise APIError(f"Request failed with status code {response.status_code}")

        res = response.json()
        items = res.get('items', [])

        results = []
        for item in items:
            temp = {
                'video_id': item['id'],
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'published_at': item['snippet']['publishedAt'],
                'view_count': item['statistics']['viewCount'],
                'like_count': item['statistics'].get('likeCount', 0),
                'comment_count': item['statistics'].get('commentCount', 0),
                'timestamp': datetime.now()
            }
            results.append(temp)

        db.insert_rows_to_db(results, dest_table, current_ds.engine, if_exists='replace')
