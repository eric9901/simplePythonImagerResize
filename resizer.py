import sys
import cv2 as cv
def resize(filepath):
        img = cv.imread(filepath)
        scale_percent = 30
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        smaller_image = cv.resize(img,dim,interpolation = cv.INTER_LINEAR) 
        cv.imshow('image', smaller_image)
        print(smaller_image.shape)
        cv.imwrite('resized.png',smaller_image,[cv.IMWRITE_PNG_COMPRESSION, 0])
        cv.waitKey(0)
        cv.destroyAllWindows()
        sys.exit()