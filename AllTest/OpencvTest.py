import cv2

#加载图片
image = cv2.imread('./timg.jpg')

#转换成灰度,提高计算速度
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#加载haar特征分类器
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

#检测图片中的人脸
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=10,
    minSize=(1,1)
)

for (x,y,w,h)in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()