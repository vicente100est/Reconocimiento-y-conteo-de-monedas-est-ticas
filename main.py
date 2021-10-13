import cv2
from cv2 import cv2
import numpy as np

vargauss=3
varKernel=3

original=cv2.imread('mx.jpg')
gris=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
gauss=cv2.GaussianBlur(gris, (vargauss,vargauss), 0)
canny=cv2.Canny(gauss, 60,100)

kernel=np.ones((varKernel,varKernel),np.uint8)
cierre=cv2.morphologyEx(canny,cv2.MORPH_CLOSE, kernel)

contornos, jerariquia=cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print("Monedas encontradas: {}".format(len(contornos)))

cv2.drawContours(original,contornos,-1,(0,0,255),2)

#cv2.imshow("Grises",gris)
#cv2.imshow("Gauss",gauss)
#cv2.imshow("Canny",canny)
#cv2.imshow("Cierre",cierre)
cv2.imshow("Resultado",original)
cv2.wagit itKey(0)