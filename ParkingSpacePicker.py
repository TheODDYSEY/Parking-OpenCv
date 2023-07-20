# import image of parking space
# mark every parking space as Region Of Interest
# works with fixed camera
import cv2
import pickle

# store clicked rectangles


width, height = 107, 48

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y+height:
                posList.pop(i)

    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)


while True:
    # create rectangle in exact positions
    # cv2.rectangle(img,(50,192),(157,240),(255,0,255),2)

    img = cv2.imread("./media/carParkImg.png")
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height),(255,0,255),2)

    cv2.imshow("image",img)
    cv2.setMouseCallback("image", mouseClick)
    cv2.waitKey(1)

print("code executed")
