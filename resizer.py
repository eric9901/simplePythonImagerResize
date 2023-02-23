import cv2
from os.path import isfile, join
def tgResize(path):
        img=cv2.imread(path)
        height= 512
        width= 512
        dim =(height,width)
        smaller_image = cv2.resize(img,dim,interpolation = cv2.INTER_LINEAR)
        oPath=join("Output",str(path)[6:-3]+"png") 
        cv2.imwrite(oPath,smaller_image,[cv2.IMWRITE_PNG_COMPRESSION, 1])
        if isfile(oPath):
                print(oPath)
        else:
                print("not file")          
def resize(StickerFormat,path):
        if StickerFormat=='tg':
                tgResize(path)