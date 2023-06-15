import requests
from models.book import Book
from utils.api_helpers import build_url


class BookAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_book_details(self, book_id):
        url = build_url(self.base_url, f"books/{book_id}")
        response = requests.get(url)
        return response

    def search_books(self, query):
        url = build_url(self.base_url, "books", params={"q": query})
        response = requests.get(url)
        return response

    def extract_book_details(self, book_data):
        title = book_data.get("title")
        author = book_data.get("author")
        category = book_data.get("category")
        price = book_data.get("price")

        return Book(title, author, category, price)
