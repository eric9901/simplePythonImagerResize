import sys
import cv2 as cv
import os
#para if beening a class
#img=
#height
#width
#format
def tgResize(img):
        height= 512
        width= 512
        dim =(height,width)
        smaller_image = cv.resize(img,dim,interpolation = cv.INTER_LINEAR) 
        #cv.imwrite(os.path.join("\Output" , 'resized.png'), img)
        cv.imwrite('resized.png',smaller_image,[cv.IMWRITE_PNG_COMPRESSION, 1])
        cv.waitKey(0)
        cv.destroyAllWindows()
        sys.exit()
def resize(StickerFormat,path):
        if StickerFormat=='tg':
                img=cv.imread(path)
                tgResize(img)
