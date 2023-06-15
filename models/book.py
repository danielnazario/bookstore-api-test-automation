class Book:
    def __init__(self, title, author, category, price):
        self.title = title
        self.author = author
        self.category = category
        self.price = price

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Category: {self.category}, Price: {self.price}"
