import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('foto.png',0)

difu = np.ones((5,5),np.float32)/25

difumi = cv2.filter2D(img,-1,difu)
laplacian = cv2.Laplacian(difumi,cv2.CV_64F)
sobelx = cv2.Sobel(difumi,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(difumi,cv2.CV_64F,0,1,ksize=5)
edges = cv2.Canny(difumi,30,40)

plt.subplot(2,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,6),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplaciana'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,4),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,5),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,2),plt.imshow(difumi,cmap = 'gray')
plt.title('Difuminada'), plt.xticks([]), plt.yticks([])
plt.subplot(2,3,3),plt.imshow(edges,cmap = 'gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])

plt.show()
