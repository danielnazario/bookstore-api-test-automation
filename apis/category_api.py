import requests
from utils.api_helpers import build_url


class CategoryAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_category_details(self, category_id):
        url = build_url(self.base_url, f"categories/{category_id}")
        response = requests.get(url)
        return response

    def search_categories(self, query):
        url = build_url(self.base_url, "categories", params={"q": query})
        response = requests.get(url)
        return response
    