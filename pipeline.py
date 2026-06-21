import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_raw_data(self, symbol):
        pass

class DataTransformer:
    def transform_raw_payload(self, raw_data):
        pass
