#Saving images from videos sources using python and openCV
#import the necessary libraries
#cv2 package for image 
import cv2
# os package to create the path to save image
import os

# path to the video source
video = '/home/guru/Downloads/face_detection_video/video.mp4'
#path to save the output image
output_path = '/home/guru/Desktop/video/'
#invoke opencv to capture the video
video_source = cv2.VideoCapture(video)
count = 0
# start looping to capture the image and its counter as <image> and <success> and while success is true
# keep writing the images on disk using cv2.imwrite
while video_source.isOpened():
	success , image = video_source.read()
	if success :
		cv2.imwrite(os.path.join(output_path ,'%d.png')  %count , image)
		count +=1
	else:
		break #to greak out of the while loop once the image has fully been written on disk
cv2.destroyAllWindows()
video_source.release()	
