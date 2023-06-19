import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def search_books(book_name):
    urls = ["https://www.yes24.com/Product/Search", "https://www.aladin.co.kr/search/wsearchresult.aspx", "https://search.kyobobook.co.kr/web/search"]
    encoded_book_name = quote(book_name)

    for url in urls:
        if 'yes24' in url:
            search_url = url + '?domain=ALL&query=' + encoded_book_name
        elif 'aladin' in url:
            search_url = url + '?SearchTarget=All&SearchWord=' + encoded_book_name + '&x=0&y=0'
        elif 'kyobobook' in url:
            search_url = url + '?keyword=' + encoded_book_name + '&gbCode=TOT&target=total'

        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        if 'yes24' in url:
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

        elif 'aladin' in url:
            book_list = soup.find('div', {'id': 'Search3_Result'})
            books = book_list.find_all('div', {'class': 'ss_book_box'})[:10]

            for book in books:
                title_tag = book.find('a', {'class': 'bo3'})
                price_tag = book.find('span', {'class': 'ss_p2'})

                title = title_tag.text.strip()
                price = price_tag.text.strip()

                print('Title:', title)
                print('Price:', price)
                print()

        elif 'kyobobook' in url:
            book_list = soup.find('div', {'id': 'shopData_list'})
            books = book_list.find_all('li', {'class': 'prod_item'})[:10]

            for book in books:
                title_tag = book.find('a', {'class': 'prod_info'})
                price_tag = book.find('span', {'class': 'val'})

                title = title_tag.text.strip()
                price = price_tag.text.strip()

                print('Title:', title)
                print('Price:', price)
                print()

book_name = input("Enter the book name: ")
search_books(book_name)
