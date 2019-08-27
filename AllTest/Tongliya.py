import tensorflow as tf
from bs4 import BeautifulSoup
import cv2,os
import numpy as np
import requests,re

url = 'https://image.baidu.com/search/index?' \
      'tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&' \
      'fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=' \
      '1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=' \
      'utf-8&word=%E4%BD%9F%E4%B8%BD%E5%A8%85&oq=%E4%BD%9F%E4%B8%BD%E5%A8%85&rsp=-1'

response = requests.get(url=url)
str = response.text

soup = BeautifulSoup(response.text,'html.parser')

pattern = re.compile(r'"objURL":".*?"')
n = 1
a = soup.find_all('script')

result = []
for i in a:
    if pattern.findall(i.decode()):
        for j in pattern.findall(i.decode()):
            result.append(j.strip('"objURL":'))
print(result)
num = 0
for url in result:
    num += 1
    path = './.img'
    content = requests.get(url=url).content
    with open(path,'wb') as f:
        f.write(content)

    img = cv2.imread(path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.1,
                                          minNeighbors=10,
                                          minSize=(50,50))
    if len(faces) != 0:
        for (x,y,w,h) in faces:

            # cv2.imshow('img',img)
            # cv2.waitKey(0)
            if not os.path.exists('./TongLiYa'):
                os.mkdir('./TongLiYa')
            if not os.path.exists('./TongLiYa/face'):
                os.mkdir('./TongLiYa/face')
            imgpath = './TongLiYa/{}'.format(url.split('/')[-1])
            print(imgpath)
            cv2.imwrite('./TongLiYa/face/face{}.jpg'.format(num), img[y - 10:y + h + 10, x - 10:x + w + 10])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.imwrite('./TongLiYa/{}.jpg'.format(url.split('/')[-1].split('.')[0]),img)
