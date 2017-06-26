import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

index = 3
filenames = ['sample1.pgm','sample2.pgm','sample3.pgm','my_favorite.jpg']
imgs = []
luminances = []

for filename in filenames:
    img = cv.imread("./imgs/"+filename)
    cv.imwrite("./imgs/"+filename+".png",img)
    imgs.append(cv.cvtColor(img,cv.COLOR_RGB2GRAY))

for i in range(len(imgs)):
    img = np.reshape(imgs[i],(1,np.product(imgs[i].shape)))[0]
    luminances.append(np.zeros(256))
    for luminance in range(256):
        luminances[i][luminance] = len(img[img==luminance])

cv.imshow(filenames[index],imgs[index])
y = luminances[index]
plt.bar(range(256),y,align='center')
plt.xlabel("luminance")
plt.ylabel("number of pixel")
plt.title("histgram of luminance about "+filenames[index])
plt.show()
