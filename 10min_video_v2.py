#Imports
import argparse
import cv2 as cv
import os
import time
import datetime

#argument parser
parser=argparse.ArgumentParser()
#time of video in minutes
parser.add_argument("-t", "--time", type=int, default=10, help="time of video in minutes default=10minutes ")
parser.add_argument("-c,","--camera", type=int, default=0, help="camera port default=0")
capture_time=parser.parse_args().time #time of video in seconds
camera_port=parser.parse_args().camera
print (capture_time," minutes of video will be recorded")
i=0 #counter for the number of videos recorded
x=0 #variable for stopping the loop
video_time=capture_time*60 -(20*capture_time)#time of video in seconds

while x==0 :
    start_time=time.time()
    elapsed_time=start_time+video_time
    
    #lets create the output folder 
    day=datetime.date.today()
    #lets make a folder for today if it doesnt exist if extant then do nothing
    
    if os.path.isdir(str(day))==True:
        print("folder exists")
    else:
        os.mkdir(str(day))
        print("folder created")
    
    #change the working directory to the folder for today
   

    #the folderday has been created 
    #now lets create the video file name
    

    
    
    now=datetime.datetime.now()
    video_title_end=now+datetime.timedelta(minutes=capture_time)
    video_title=now.strftime("%H-%M") + "_" + video_title_end.strftime("%H-%M") + ".mp4"
    #print(video_title)
    
    video_title.strip(":")
    # Start capturing video from the default webcam
    cap = cv.VideoCapture(camera_port)
    # Define the codec and create VideoWriter object
    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    
    os.chdir(os.getcwd()+"/"+str(day))
    out = cv.VideoWriter(video_title, fourcc, 20.0, (640,  480))

    print(os.getcwd())


    while  cap.isOpened() and elapsed_time > time.time() :
        
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        else:
            frame = cv.flip(cv.flip(frame, 0),0)
            # write the flipped frame
            out.write(frame)
            cv.imshow('frame', frame)
        
        if cv.waitKey(1) == ord('q'):
            x=1
            break
    else:
        cap.release()
        out.release()
        os.chdir("..")
    cv.destroyAllWindows()
    