import cv2
import numpy as np

#Read two separate images
img1 = cv2.imread("dogs.jpg")
img2 = cv2.imread("mum.jpg")

#Resize images so they have equal size
img3 = cv2.resize(img1, (600,600))
img4 = cv2.resize(img2, (600,600))


#Function that takes the image to show first and image to show last.
#Function then varies their weighting so images can blend from 1st to 2nd

def slideShow(imgPre, imgPost):
	weight1 = 1
	weight2 = 0
	while weight2 < 1:
		dst = cv2.addWeighted(imgPre, weight1, imgPost, weight2, 0)
		cv2.imshow("blended img", dst)
		cv2.waitKey(500)

		weight1 = weight1 - 0.1
		weight2 = weight2 + 0.1


	cv2.imshow("blended img", dst)
	cv2.waitKey(0)


#Calling the function
slideShow(img3, img4)







