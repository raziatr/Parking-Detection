"""
script ini untuk membuat bounding pada gambar, 
jalankan sekali saja.
"""

import cv2
import pickle

# kedua variable ini untuk mengatur ukuran bounding box
width,height = 80,30
try:
    with open("ParkPos","rb") as f:
        pos_list = pickle.load(f)

except:
    pos_list = []

def mouse_click(events,x,y,flags,params):
    if events ==cv2.EVENT_LBUTTONDOWN:
        pos_list.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(pos_list):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                pos_list.pop(i)

    with open("ParkPos","wb") as f:
        pickle.dump(pos_list,f)

while True:
    image = cv2.imread("carParkingReal.jpg")

    for pos in pos_list:
        cv2.rectangle(image, pos, (pos[0]+width,pos[1]+height),(255,0,255),2)


    cv2.imshow("image",image)
    cv2.setMouseCallback("image",mouse_click)
    cv2.waitKey(1)
