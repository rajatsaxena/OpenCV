#to capture a video, you need to create VideoCapture object.

import numpy as np
import cv2

cap=cv2.VideoCapture()

while(True):
		#capture frame-by-frame
		ret, frame= cap.read()
	
		#operation on frame
		gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		#displays the resulting frame
		cv2.imshow('frame',gray)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

#after doing everything release the capture
cap.release()
cv2.destroyAllWindows()





#u can also access some of the features of video usign cap.get(propID) method where propId is a number from 0 to 18. each number displays a property of video.
