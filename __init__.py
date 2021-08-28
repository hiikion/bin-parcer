from bs4 import BeautifulSoup
import requests


# pastebinOmatic by hiikion aka hkon
# v1.2
# mpl 2.0 licence 


# pastebin integration added in 1.0
class pastebin:
    
    def __init__(self, url):
        self.url = url


    def password_check(self):
        page = requests.get(self.url).text
        if 'Locked Paste' in page:
            return True
        else:
            return False

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



# ghostbin.com integration added in 1.2
class ghostbin:

    def __init__(self, url):
        self.url = url

    def password_check(self):
        page = requests.get(self.url).content
        soup = BeautifulSoup(page, 'html.parcer')
        if soup.find('div', class_='container').text.replace('"', '') == 'Encrypted pastes have this format: ghostbin.com/<pasteId>/<password>':
            return True
        else:
            return False

    def get_title(self):
        page = requests.get(self.url).content
        soup = BeautifulSoup(page, 'html.parcer')
        try:
            title = soup.find('h4')
            return title.text
        except:
            return None

    def get_content(self):
        page = requests.get(self.url).content
        soup = BeautifulSoup(page, 'html.parcer')
        content = soup.find('textarea', class_='form-control')
        return content.text
