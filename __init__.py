from bs4 import BeautifulSoup
import requests
import random

# pastebinOmatic by hiikion aka hkon
# v1.1
# mpl 2.0 licence 

class parce:
    
    def __init__(self, url):
        self.url = url


    def get_content(self):
        
        page = requests.get(self.url).content

        soup = BeautifulSoup(page, 'html.parser')

        content = soup.find('textarea', class_='textarea')

        return content.text


    def get_title(self):
        page = requests.get(self.url).content

        soup = BeautifulSoup(page, 'html.parser')

        title = soup.find('h1')

        return title.text

    def get_author(self):

        page = requests.get(self.url).content

        soup = BeautifulSoup(page, 'html.parser')

        author = soup.find('div', class_='username')

        return author.text.strip()

    def get_date(self):
        page = requests.get(self.url).content

        soup = BeautifulSoup(page, 'html.parser')

        date = soup.find('div', class_='date')

        return date.text.strip().replace(' ', '')

    def get_views(self):
        page = requests.get(self.url).content

        soup = BeautifulSoup(page, 'html.parser')

        views = soup.find('div', class_='visits')

        return int(views.text)

    def get_expire_date(self):
        page = requests.get(self.url).content

        soup = BeautifulSoup(page, 'html.parser')

        exp_date = soup.find('div', class_='expire')

        return exp_date.text.strip().replace(' ', '')

    def get_syntax_hilight(self):
        page = requests.get(self.url).content

        soup = BeautifulSoup(page, 'html.parser')

        shl = soup.find('a', class_='btn -small h_800')

        return shl.text

'''
class api:
    
    def __init__(self, api_key):
        self.api_key = str(api_key)

    def create(self, text, title, view, expire, syntax_hilight):
        self.text = str(text)
        self.title = str(title)
        self.view = int(view)
        self.expire = str(expire)
        self.syntax_hilight = str(syntax_hilight)


        postc = {
            'api_dev_key': self.api_key,
            'api_paste_code': self.text,
            'api_paste_private': self.view,
            'api_paste_name': self.title,
            'api_paste_expire_date': self.expire,
            'api_paste_format': self.syntax_hilight,
            'api_user_key': self.api_key,
            'api_option': 'paste'
        }

        
'''
