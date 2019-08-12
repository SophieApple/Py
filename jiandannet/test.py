import sys,requests,time,os
from bs4 import BeautifulSoup

srclist = []
for i in range(10):
    try:
        re = requests.get('http://jandan.net/pic/page-{}#comments'.format(i)).text
    except:
        continue
    soup = BeautifulSoup(re,'lxml')
    img = soup.find_all('img')
    for j in img:
        srclist.append(j['src'])

# print(srclist)

for i in srclist:
    print(i.split('/')[-1])

if not os.path.exists('./pic'):
    os.mkdir('./pic')

for i in srclist:
    try:
        with open('./pic/{}'.format(i.split('/')[-1]),'wb') as f:
            f.write(requests.get('http:{}'.format(i)).content)
            print('{} done!'.format(i.split('/')[-1]))
    except:
        print('{} error...'.format(i.split('/')[-1]))