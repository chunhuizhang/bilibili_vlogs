import cv2
import numpy as np

src = cv2.imread("sample_person.jpg")
src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
r = cv2.selectROI('input', src, False)  # 返回 (x_min, y_min, w, h)

# roi区域
roi = src[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
img = src.copy()
cv2.rectangle(img, (int(r[0]), int(r[1])), (int(r[0]) + int(r[2]), int(r[1]) + int(r[3])), (255, 0, 0), 2)

# 原图mask
mask = np.zeros(src.shape[:2], dtype=np.uint8)
# 矩形roi
rect = (int(r[0]), int(r[1]), int(r[2]), int(r[3]))  # 包括前景的矩形，格式为(x,y,w,h)

background = cv2.imread("sample_giraffe.jpg")

h, w, ch = src.shape
background = cv2.resize(background, (w, h))
# cv.imwrite("background.jpg", background)

# mask = np.zeros(src.shape[:2], dtype=np.uint8)
bgdmodel = np.zeros((1, 65), np.float64)
fgdmodel = np.zeros((1, 65), np.float64)

cv2.grabCut(src, mask, rect, bgdmodel, fgdmodel, 5, mode=cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 1) | (mask == 3), 255, 0).astype('uint8')

# 高斯模糊，边缘变得光滑
se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
cv2.dilate(mask2, se, mask2)
mask2 = cv2.GaussianBlur(mask2, (5, 5), 0)
cv2.imshow('background-mask', mask2)
# cv.imwrite('background-mask.jpg', mask2)

# 虚化背景
# background = cv.GaussianBlur(background, (0, 0), 3)
mask2 = mask2 / 255.0
print('mask2 shape', mask2.shape)
a = mask2[..., None]
print('a shape', a.shape)

# 融合方法 com = a*fg + (1-a)*bg
result = a * (src.astype(np.float32)) + (1 - a) * (background.astype(np.float32))
# result = cv2.bitwise_and(background.astype(np.uint8), background.astype(np.uint8), mask=mask2)

cv2.imshow("result", result.astype(np.uint8))
cv2.imwrite("result.jpg", result.astype(np.uint8))

cv2.waitKey(0)
cv2.destroyAllWindows()
