import sys,requests,time,os
from bs4 import BeautifulSoup


def getpic(start=0,end=10):
    srclist = []


    for i in range(start,end):
        try:
            re = requests.get('http://jandan.net/pic/page-{}#comments'.format(i)).text
        except:
            continue
        soup = BeautifulSoup(re,'lxml')
        img = soup.find_all('img')
        for j in img:
            srclist.append(j['src'])

    # print(srclist)

    # for i in srclist:
    #     print(i.split('/')[-1])

    if not os.path.exists('./pic'):
        os.mkdir('./pic')
    succes = []
    fail = []
    exist = []

    for i in srclist:
        if not os.path.exists('./pic/{}'.format(i.split('/')[-1])):
            try:
                with open('./pic/{}'.format(i.split('/')[-1]),'wb') as f:
                    f.write(requests.get('http:{}'.format(i)).content)
                    print('{} done!'.format(i.split('/')[-1]))
                    succes.append(i.split('/')[-1])
            except:
                print('{} error...'.format(i.split('/')[-1]))
                fail.append(i.split('/')[-1])
        else:
            print('file {} exists!'.format(i.split('/')[-1]))
            exist.append(i.split('/')[-1])
    print("""
    succes:{}
    fail:{}
    exist:{}
    """.format(len(succes),len(fail),len(exist)))


if __name__ == '__main__':
    getpic()