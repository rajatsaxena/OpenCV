import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

#img= cv2.imread('test.jpg')
cap = cv2.VideoCapture(0)

while(True):
	ret, img = cap.read() 
	gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	faces = face_cascade.detectMultiScale(gray_img, 1.05, 5)
	print faces
	 
	for (p,q,r,s) in faces:
		cv2.rectangle(img,(p,q),(p+r,q+s),(255,0,0),2)
		face_gray = gray_img[q:q+s, p:p+r] 
		face_color = img[q:q+s, p:p+r] 
		eyes = eye_cascade.detectMultiScale(face_gray) 
	 	for (ep,eq,er,es) in eyes:
			cv2.rectangle(face_color,(ep,eq),(ep+er,eq+es), (0,255,0),2)
		nose = nose_cascade.detectMultiScale(face_gray)
		#print "nose:" + str(nose)
		for (np,nq,nr,ns) in nose:
			cv2.rectangle(face_color,(np,nq),(np+nr,nq+ns), (0,0,0),2)
		mouth = mouth_cascade.detectMultiScale(face_gray)
		#print "mouth:" + str(mouth)
		for (mp,mq,mr,ms) in mouth:
			cv2.rectangle(face_color,(mp,mq),(mp+mr,mq+ms), (255,255,255),2)
	 
	cv2.imshow("output", img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
