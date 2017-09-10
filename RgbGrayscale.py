import cv2

image = cv2.imread('H:\semester5\pcd\Tugas_UTS_pcd\contoh.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('sufriRgbGreyscale.jpg', gray)
