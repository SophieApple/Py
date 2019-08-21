import cv2,sys,time,os

def AnalysisImg(imgpath,savepath):
    img_name = time.strftime('%H%M%S')
    print(img_name)
    print(imgpath)

    img = cv2.imread(imgpath)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(50,10)
    )
    if len(faces) > 0:
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.imwrite('{}{}.jpg'.format(savepath,img_name), img)


for (root,dirs,files) in os.walk('./pic'):
    pass

test = []
n = 0
for i in files:
    if i.split('.')[1] in ['jpg','png']:
        test.append(i)
        n += 1
print(test)
print(n)

for i in test:
    AnalysisImg('./pic/{}'.format(i),'./save/')