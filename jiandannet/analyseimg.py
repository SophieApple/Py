import requests
from bs4 import BeautifulSoup


class analyseUrl():
    """
    分析url结构获取
    """
    def __init__(self):
        self.imgurl = []
        self.imglistb = []
        pass

    def get(self, url='http://jiandan.net/pic'):
        self.reaponse = requests.get(url).text
        self.soup = BeautifulSoup(self.reaponse, 'lxml')
        self.img = self.soup.find_all('img')
        for i in self.img:
            print(i['src'])
            self.imgurl.append(i['src'])
        for i in self.imgurl:
            url = 'http:{}'.format(i)
            self.imglistb.append(requests.get(url).content)
