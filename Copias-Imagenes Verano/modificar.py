#import the necessary modules
import cv2
#import freenect
from matplotlib import pyplot as plt
import numpy as np


img = cv2.imread('foto.png',0)
#cv2.imshow('Foto',img)

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Nueva')
plt.xticks([]), plt.yticks([])
plt.show()
#k = cv2.waitKey(0) & 0xFF

#if k == 27:
 #       cv2.imwrite('fotonew.png',dst)
#cv2.destroyAllWindows()
