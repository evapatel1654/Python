from domain.book import Book
from repository.json_repository import JsonBookRepository
from service.book_service import BookService


repo = JsonBookRepository('data/books.json')
service = BookService(repo)


while True:
cmd = input('> ').lower()


if cmd == 'add':
book = Book(
book_id=input('ID: '),
title=input('Title: '),
author=input('Author: ')
)
service.create_book(book)


elif cmd == 'list':
for b in service.list_books():
print(b)


elif cmd == 'checkout':
service.checkout_book(input('Book ID: '))


elif cmd == 'exit':
break
