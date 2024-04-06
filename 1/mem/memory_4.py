from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int

    # Инстанс-метод
    def description(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    # Класс-метод
    @classmethod
    def from_string(cls, book_str):
        title, author, pages = book_str.split(', ')
        return cls(title, author, int(pages))

    # Статический метод
    @staticmethod
    def is_book_valid(book):
        return book.pages > 0 and bool(book.title) and bool(book.author)

    # Специальный метод
    def __str__(self):
        return f"'{self.title}' by {self.author}"
