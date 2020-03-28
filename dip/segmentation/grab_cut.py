import cv2
import numpy as np

src = cv2.imread("sample_person.jpg")
src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)

# 交互式，返回 (x_min, y_min, w, h)
r = cv2.selectROI('input', src, True)

# roi区域
roi = src[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

# 原图mask，与原图等大小
mask = np.zeros(src.shape[:2], dtype=np.uint8)

# 矩形roi
rect = (int(r[0]), int(r[1]), int(r[2]), int(r[3]))  # 包括前景的矩形，格式为(x,y,w,h)

# bg模型的临时数组
bgdmodel = np.zeros((1, 65), np.float64)
# fg模型的临时数组
fgdmodel = np.zeros((1, 65), np.float64)

cv2.grabCut(src, mask, rect, bgdmodel, fgdmodel, 11, mode=cv2.GC_INIT_WITH_RECT)

print(np.unique(mask))
# 提取前景和可能的前景区域
mask2 = np.where((mask == 1) | (mask == 3), 255, 0).astype('uint8')

print(mask2.shape)

# 按位与 src & src == 0，得到的是二进制
result = cv2.bitwise_and(src, src, mask=mask2)
# cv2.imwrite('result.jpg', result)
# cv2.imwrite('roi.jpg', roi)

cv2.imshow('mask', mask2)
cv2.imshow('roi', roi)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
