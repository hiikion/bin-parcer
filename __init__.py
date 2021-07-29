from bs4 import BeautifulSoup
import requests

# pastebinOmatic by hiikion aka hkon
# v1.0
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

        return author.text

    def get_date(self):

        page = requests.get(self.url).content

        soup = BeautifulSoup(page, 'html.parser')

        date = soup.find('div', class_='date')

        return date.text

    def get_views(self):

        page = requests.get(self.url).content

        soup = BeautifulSoup(page, 'html.parser')

        views = soup.find('div', class_='visits')

        return views.text

    def get_expire_date(self):

        page = requests.get(self.url).content

        soup = BeautifulSoup(page, 'html.parser')

        exp_date = soup.find('div', class_='expire')

        return exp_date.text

    def get_syntax_hilight(self):

        page = requests.get(self.url).content

        soup = BeautifulSoup(page, 'html.parser')

        shl = soup.find('a', class_='btn -small h_800')

        return shl.text


'''
class api:
    soon...
'''
