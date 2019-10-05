import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/45479/Desktop/learn/lesson01/111.jpg', 1)

#plt show
B,G,R = cv2.split(img)
img_rgb = cv2.merge((R,G,B))
plt.imshow(img_rgb)
plt.show()

# image crop
img_crop = img[200:400, 200:500]

# change color
def random_light_color(img):
    # brightness
    B, G, R = cv2.split(img)
    data = [B, G, R]
    for i in data:
        rand_ = random.randint(-50, 50)
        if rand_ == 0:
            pass
        elif rand_ > 0:
            lim = 255 - rand_
            i[i > lim] = 255
            i[i <= lim] = (rand_ + i[i <= lim]).astype(img.dtype)
        elif rand_ < 0:
            lim = 0 - rand_
            i[i < lim] = 0
            i[i >= lim] = (rand_ + i[i >= lim]).astype(img.dtype)
    img_merge = cv2.merge((B, G, R))
    return img_merge

# gamma correction
def gamma_adj(img, gamma = 1.0):
    inv_gamma = 1/gamma
    table = []
    for i in range(256):
        table.append((i/255.0)**inv_gamma*255.0)
    table = np.array(table).astype("uint8")
    return cv2.LUT(img, table)

# histogram code
plt.hist(img.flatten(), 256, [0, 256])

#change color in YUV space
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
Y, U, V = cv2.split(img_yuv)
for i in Y:
    i[i>200] = i[i>200] - 100
img_yuv2 = cv2.merge((Y, U, V))
img_output = cv2.cvtColor(img_yuv2, cv2.COLOR_YUV2BGR)   # y: luminance(明亮度), u&v: 色度饱和度

#rotation + scale
M = cv2.getRotationMatrix2D((img.shape[1]/2, img.shape[0]/2), 30, 0.5)
img_rotation = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))


# useing three  points to transform
rows, cols, ch = img.shape
pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
pts2 = np.float32([[cols * 0.2, rows * 0.1], [cols * 0.9, rows * 0.2], [cols * 0.1, rows * 0.9]])
# M is the transfor_matrix
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))



#Combine image crop, color shift, rotation and perspective transform together to complete a data augmentation script
img1 = cv2.imread('C:/Users/45479/Desktop/learn/lesson01/111.jpg', 1)
cv2.imshow('src',img1)
cv2.waitKey()

img_2 = img1[100:400,200:500]
cv2.imshow('crop',img_2)
cv2.waitKey()

B, G, R = cv2.split(img_2)
for i in B:
    i[i>200] = i[i>200] - 100
img_3 = cv2.merge((B, G, R))
cv2.imshow('color shift',img_3)
cv2.waitKey()

Matrix_ = cv2.getRotationMatrix2D((50, 50), 30, 1.5)
img_rotation_ = cv2.warpAffine(img_3, M, (img.shape[1], img.shape[0]))
cv2.imshow('rotation',img_rotation_)
cv2.waitKey()

rows, cols, ch = img_rotation_.shape
pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])
pts2 = np.float32([[cols * 0.2, rows * 0.1], [cols * 0.9, rows * 0.2], [cols * 0.1, rows * 0.9], [cols * 0.6, rows * 0.6]])
# M_warpis the transfor_matrix
M_warp = cv2.getPerspectiveTransform(pts1, pts2)
img_warp = cv2.warpPerspective(img_rotation_, M_warp, (cols, rows))
cv2.imshow('perspective transform',img_warp)
cv2.waitKey()
