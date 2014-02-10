#we create a videowriter object

import numpy as np
import cv2


#define the codec and creating a video writer object
fourcc=cv2.VideoWriter_fource(*'XVID')
out= cv2.VideoWriter('output.avi',fource,20.0,(640,480))

while(cap.isOpened()):
	ret, frame= cap.read()
	if ret==True:
		frame=cv2.flip(frame, 0)

		#write the flipped frame
		out.write(frame)

		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q):
			break
	else:
		break


#release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()


