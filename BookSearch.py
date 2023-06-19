import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def search_books(url, book_name):
    encoded_book_name = quote(book_name)

    if 'yes24' in url:
        search_url = url + '?domain=ALL&query=' + encoded_book_name
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        book_list = soup.find('ul', {'id': 'yesSchList'})
        books = book_list.find_all('li')[:10]

        for book in books:
            title_tag = book.find('a', {'class': 'gd_name'})
            price_tag = book.find('em', {'class': 'yes_b'})

            title = title_tag.text.strip()
            price = price_tag.text.strip()

            print('Title:', title)
            print('Price:', price)
            print()

book_name = input("Enter the book name: ")
search_books("https://www.yes24.com/Product/Search", book_name)
