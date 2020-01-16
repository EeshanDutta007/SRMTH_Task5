import cv2
import numpy as np

def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: 
        colors = image[y,x]
        yuv = np.uint8([[colors]])
        YUV = cv2.cvtColor(yuv,cv2.COLOR_BGR2YUV)  
        print("YUV Format: ",YUV)

cap=cv2.VideoCapture(0)
_, k=cap.read()
while(_):
    _, k=cap.read()
    cv2.imshow("Image",k)
    if(cv2.waitKey(5)==27):
        cv2.imwrite("1.jpg",k)
        break
image = cv2.imread("1.jpg")
cv2.namedWindow('IMAGE')
cv2.setMouseCallback('IMAGE',mouseRGB)


while(True):
    cv2.imshow('IMAGE',image)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()