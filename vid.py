import numpy as np 
import cv2 
my_cap = cv2.VideoCapture(D:\Downloads\Countdown 
Timer.mov") 
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
output = cv2.VideoWriter('output.avi',fourcc, 20.0, 
(640,480)) 
while(True): 
 ret, my_frame = my_cap.read() 
 gray = cv2.cvtColor(my_frame, cv2.COLOR_BGR2GRAY) 
 output.write(my_frame) 
 cv2.imshow('my_frame',gray) 
 if cv2.waitKey(1) & 0xFF == ord('q'): 
 break 
my_cap.release() 
output.release() 
cv2.destroyAllWindows()
