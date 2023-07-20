import cv2
import pickle
import cvzone
import numpy as np

# video feed
cap = cv2.VideoCapture('./media/carPark.mp4')

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

width, height = 107, 48


def checkParkingSpace(imgPro):

    spaceCounter = 0;

    for pos in posList:
        x, y = pos

        # cropping the images
        imgCrop = imgPro[y:y+height,x:x+width]
        # cv2.imshow(str(x*y), imgCrop)

        # count the pixels in each parking place
        count = cv2.countNonZero(imgCrop)

        # put count of pixels of each place in rectangles
        cvzone.putTextRect(img,str(count),(x,y+height-5), scale=1.5, thickness=2, offset=0, colorR=(0,0,255))

        if count < 900:
            color = (0,255,0)
            thickness = 5
            spaceCounter += 1

        else:
            color = (0,0,255)
            thickness = 2


    # put count of pixels of each place in rectangles
    cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), color, thickness)
    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}' ,(100, 50), scale=3, thickness=5, offset=20, colorR=color)

while True:

    # infinite loop video
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)

    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3,3), 1)

    # converting image to binary (white lines on black bg)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,25,16)

    # clear out the "noise" pixels
    imgMedian = cv2.medianBlur(imgThreshold, 5)

    kernel = np.ones((3,3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    checkParkingSpace(imgDilate)

    # for pos in posList:
        # cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height),(255,0,255),2)

    cv2.imshow("Image", img)
    cv2.imshow("ImageBlur", imgBlur)
    cv2.imshow("ImageThresh", imgMedian)

    # slows down the video
    cv2.waitKey(10)
