import cv2
from os.path import isfile, join
def tgResize(path):
        img=cv2.imread(path)
        cv2.imshow('img',img)
        cv2.waitKey(1000)
        print(img)
        height= 512
        width= 512
        dim =(height,width)
        smaller_image = cv2.resize(img,dim,interpolation = cv2.INTER_LINEAR)
        print("start write img: "+"Output/"+str(path)[6:-3]+"png") 
        cv2.imwrite("Output/"+str(path)[6:-3]+"png",smaller_image,[cv2.IMWRITE_PNG_COMPRESSION, 1])
        img=cv2.imread("Output/"+str(path)[6:-3]+"png")
        cv2.imshow('img',img)
        cv2.waitKey(1000)
        if isfile(join("Output/", str(path)[6:-3]+"png")):
                print(join("Output/", str(path)[6:-3]+"png"))
        else:
                print("not file")
                
        print("Finish write img: "+"Output/"+str(path)[6:-3]+"png") 
def resize(StickerFormat,path):
        if StickerFormat=='tg':
                print("start resize:tg")
                tgResize(path)