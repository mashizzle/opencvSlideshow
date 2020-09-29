import cv2
import numpy as np

img = cv2.imread("cards.jpg")




def mousePosition(event, x,y, flags, param):
	global x1,x2,y1,y2
	if event == cv2.EVENT_LBUTTONDOWN:
		x1 = x
		y1 = y
		print(x1,y1)
		
	elif event == cv2.EVENT_LBUTTONUP:
		x2 = x
		y2 = y
		print(x2,y2)

		cv2.rectangle(img, (x1,y1),(x2,y2), (255,0,0,0),cv2.LINE_4)


cv2.imshow("Unaltered", img)  # this needs to be here before the while loop for some reason??
cv2.setMouseCallback("Unaltered", mousePosition)
while(1):
	cv2.imshow("Unaltered",img)
	k =cv2.waitKey(1) & 0xFF
	if k == ord('m'):
		break

cv2.destroyAllWindows()

