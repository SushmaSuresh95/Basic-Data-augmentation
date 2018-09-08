import cv2
import numpy as np
#Add your image path in the line below and run the code
pic = cv2.imread("<add your image path here>", 1)

#Original Image
resize_pic = cv2.resize(pic, (256,256))
cv2.imshow('Original Color Image' ,resize_pic)
pic1 = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)

#Grayscale Image
resize_pic1 = cv2.resize(pic1, (256,256))
cv2.imshow('Grayscale' ,resize_pic1)
cv2.imwrite('Grayscale.png',resize_pic1)

#Threshold Color Image
retval, threshold = cv2.threshold(resize_pic,125,255,cv2.THRESH_BINARY)
cv2.imshow('Threshold-Color Image', threshold)
cv2.imwrite('Threshold_color.png',threshold)

#Threshold Grayscale image
retval, thresholdnew = cv2.threshold(resize_pic1,125,255,cv2.THRESH_BINARY)
cv2.imshow('Threshold-Grayscale Image', thresholdnew)
cv2.imwrite('Threshold_grayscale.png',thresholdnew)

#Inverted image
retval, inv = cv2.threshold(resize_pic1,125,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Negative Image', inv)
cv2.imwrite('Inverted.png',inv)

#Gaussian adaptive Threshold for high threshold value
gaus = cv2.adaptiveThreshold(resize_pic1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,225,1)
cv2.imshow('Gaussian Adaptive Threshold-high',gaus)
cv2.imwrite('Gaussian_adaptive_high.png',gaus)

#Gaussian adaptive Threshold for a low threshold value
gaus1 = cv2.adaptiveThreshold(resize_pic1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,1)
cv2.imshow('Gaussian Adaptive Threshold-low',gaus1)
cv2.imwrite('Gaussian_adaptive_low.png',gaus1)

#threshold by OTSU
retval2, otsu = cv2.threshold(resize_pic1,125,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Threshold-OTSU',otsu)
cv2.imwrite('Threshold_otsu.png',otsu)

#Blurred Image
Blur = cv2.blur(resize_pic1,(7,7))
cv2.imshow('Blurred Image', Blur)
cv2.imwrite('Blurred.png',Blur)

#Morphological Operation - Erosion
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(resize_pic1,kernel,iterations = 1)
cv2.imshow('Erosion',erosion)
cv2.imwrite('Erosion.png',erosion)

#Dilation
dilation = cv2.dilate(resize_pic1,kernel,iterations = 1)
cv2.imshow('Dilation',dilation)
cv2.imwrite('Dilation.png',dilation)

#Opening
opening = cv2.morphologyEx(resize_pic1, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening',opening)
cv2.imwrite('Opening.png',opening)

#Closing
closing = cv2.morphologyEx(resize_pic1, cv2.MORPH_CLOSE, kernel)
cv2.imshow('closing',closing)
cv2.imwrite('Closing.png',closing)

#Rotation of Image by 90 degrees
rows,cols = resize_pic1.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(resize_pic1,M,(cols,rows))
cv2.imshow('Rotation_90',dst)
cv2.imwrite('Rotation_90.png',dst)

#Rotation of Image by 180 degrees
M1 = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
dst1 = cv2.warpAffine(resize_pic1,M1,(cols,rows))
cv2.imshow('Rotation_180',dst1)
cv2.imwrite('Rotation_180.png',dst1)

cv2.waitKey(0)
cv2.destroyAllWindows()