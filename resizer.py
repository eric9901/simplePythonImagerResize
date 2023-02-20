import sys
import cv2 as cv
import os
#para if beening a class
#img=
#height
#width
#format
def tgResize(path):
        img=cv.imread(path)
        height= 512
        width= 512
        dim =(height,width)
        smaller_image = cv.resize(img,dim,interpolation = cv.INTER_LINEAR) 
        #cv.imwrite(os.path.join("\Output" , 'resized.png'), img)
        
        print("Output\\"+str(path)[6:-3]+"png")
        cv.imwrite("Output\\"+str(path)[6:-3]+"png",smaller_image,[cv.IMWRITE_PNG_COMPRESSION, 1])
def resize(StickerFormat,path):
        if StickerFormat=='tg':
                tgResize(path)
