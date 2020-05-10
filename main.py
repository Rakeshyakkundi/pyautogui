import pyautogui
from PIL import Image,ImageGrab
import time
# from numpy import asarray

def takeScreenshot():
    image = ImageGrab.grab().convert('L')
    return image

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(170,290):
        for j in range(360,370):
            if data[i,j] < 100:
                hit('down')
                return 5
    for i in range(150,270):
        for j in range(385,460):
            if data[i,j] < 100:
                hit('up')
                return True
    return False


if __name__=='__main__':
    time.sleep(1)
    while True:
        image = takeScreenshot()
        # a = asarray(image)
        data = image.load()
        h = isCollide(data)
        if h==5:
            hit('up')
            break
 
       
