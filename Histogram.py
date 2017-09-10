import cv2

image = cv2.imread('H:\semester5\pcd\Tugas_UTS_pcd\contoh.jpg')
cv2.normalize(image, image, alpha=20, beta=200, norm_type=cv2.NORM_MINMAX)
cv2.imwrite('sufriadiHistogram.jpg', image)
