import cv2
import imutils
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd =
r'/usr/local/bin/tesseract'
img = cv2.imread('toll.jpeg',cv2.IMREAD_COLOR)
img = cv2.resize(img, (600,400) )
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 13, 15, 15)
edged = cv2.Canny(gray, 30, 200)
contours = cv2.findContours(edged.copy(), cv2.RETR_TREE,
cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key = cv2.contourArea, reverse =
True)[:10]
screenCnt = None
for c in contours:

 peri = cv2.arcLength(c, True)
 approx = cv2.approxPolyDP(c, 0.018 * peri, True)
 if len(approx) == 4:
 screenCnt = approx
 if len(approx) == 4:
 screenCnt = approx
 break
if screenCnt is None:
 detected = 0
 print ("No contour detected")
else:
18
 detected = 1
if detected == 1:
 cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)
mask = np.zeros(gray.shape,np.uint8)
new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
new_image = cv2.bitwise_and(img,img,mask=mask)
(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx+5, topy:bottomy+5]
text = pytesseract.image_to_string(Cropped, config='--psm
11')
print("programming_fever's License Plate Recognition\n")