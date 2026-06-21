import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

def fetch_raw_data(self, symbol):
        full_url = f"{self.base_url}/{symbol}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(full_url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data: {response.status_code}")
            return None
    
class DataTransformer:
    def transform_raw_payload(self, raw_data):
        pass
