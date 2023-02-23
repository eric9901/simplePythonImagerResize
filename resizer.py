import cv2
from os.path import isfile, join
def tgResize(path):
        img=cv2.imread(path)
        height= 512
        width= 512
        dim =(height,width)
        smaller_image = cv2.resize(img,dim,interpolation = cv2.INTER_LINEAR)
        aPATH=join("Output", str(path)[6:-3]+"png")
        print(aPATH) 
        cv2.imwrite(aPATH,smaller_image,[cv2.IMWRITE_PNG_COMPRESSION, 1])
        img=cv2.imread(aPATH)
        if isfile(aPATH):
                print(aPATH)
        else:
                print("not file")     
        print("Finish write img: "+aPATH) 
def resize(StickerFormat,path):
        if StickerFormat=='tg':
                print("start resize:tg")
                tgResize(path)