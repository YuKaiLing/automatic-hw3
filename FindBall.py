import cv2
import numpy as np
import time as t
cp0 = cv2.VideoCapture(1)
cp0.set(3,640)
cp0.set(4,480)
row=cp0.get(3)
col=cp0.get(4)
color=raw_input([])
print color

print row,col
while 1:
    circles=None
    s=t.time()
    ret0, frame0 = cp0.read()
    (B,G,R)=cv2.split(frame0)
    ret,B=cv2.threshold(B,127,255,cv2.THRESH_BINARY)
    ret,G=cv2.threshold(G,127,255,cv2.THRESH_BINARY)
    ret,R=cv2.threshold(R,127,255,cv2.THRESH_BINARY)
    sub1=cv2.subtract(R,B)
    sub2=cv2.subtract(R,G)
    sub3=cv2.subtract(B,G)
    sub4=cv2.subtract(B,R)
    sub5=cv2.subtract(G,R)
    sub6=cv2.subtract(G,B)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(9, 9))
    if color == 'red':
        circles = cv2.HoughCircles(sub2,cv2.HOUGH_GRADIENT,2,200,param1=100,param2=65,minRadius=30,maxRadius=250)
        if np.any(circles==None):
            print 'no'
        else:
            circles = np.uint16(np.around(circles))
            red=0
            for i in circles[0,:]:
                cv2.circle(frame0,(i[0],i[1]),i[2],(255,255,255),2)
                cv2.circle(frame0,(i[0],i[1]),2,(255,255,255),3)
                for j in range(0,10):
                    for k in range(0,10):
                       (b,g,r)=frame0[np.uint16(i[1])-10+j,np.uint16(i[0])-10+k]
                       if r>127 and g-b<30:
                           red +=1
            if red>=50:
                print 'True'
                           
    elif color=='green':
        circles = cv2.HoughCircles(sub5,cv2.HOUGH_GRADIENT,2,200,param1=100,param2=80,minRadius=50,maxRadius=250)
        if np.any(circles==None):
            print 'no'
        else:
            circles = np.uint16(np.around(circles))
            green=0
            for i in circles[0,:]:
                cv2.circle(frame0,(i[0],i[1]),i[2],(255,255,255),2)
                cv2.circle(frame0,(i[0],i[1]),2,(255,255,255),3)
                for j in range(0,10):
                    for k in range(0,10):
                        (b,g,r)=frame0[np.uint16(i[1])-10+j,np.uint16(i[0])-10+k]
                        if g>127 and b<127:
                            green +=1
            if green>=50:
                print 'True'
                        
    elif color =='blue':
        circles = cv2.HoughCircles(sub4,cv2.HOUGH_GRADIENT,2,200,param1=100,param2=70,minRadius=50,maxRadius=200)
        if np.any(circles==None):
            print 'no'
        else:
            circles = np.uint16(np.around(circles))
            blue=0
            for i in circles[0,:]:
                cv2.circle(frame0,(i[0],i[1]),i[2],(255,255,255),2)
                cv2.circle(frame0,(i[0],i[1]),2,(255,255,255),3)
                for j in range(0,10):
                    for k in range(0,10):
                        (b,g,r)=frame0[np.uint16(i[1])-10+j,np.uint16(i[0])-10+k]
                        if b>127 and g<127 and r<127:
                            blue +=1
            if blue>=50:
                print 'True'
    elif color =='orange':
        circles = cv2.HoughCircles(sub1,cv2.HOUGH_GRADIENT,2,200,param1=100,param2=70,minRadius=50,maxRadius=200)
        if np.any(circles==None):
            print 'no'
        else:
            circles = np.uint16(np.around(circles))
            orange=0
            for i in circles[0,:]:
                cv2.circle(frame0,(i[0],i[1]),i[2],(255,255,255),2)
                cv2.circle(frame0,(i[0],i[1]),2,(255,255,255),3)
                for j in range(0,10):
                    for k in range(0,10):
                        (b,g,r)=frame0[np.uint16(i[1])-10+j,np.uint16(i[0])-10+k]
                        if g<127 and g-b>30:
                            orange +=1
            if orange>=50:
                print 'True'
    elif color =='yellow':
        circles = cv2.HoughCircles(sub1,cv2.HOUGH_GRADIENT,2,200,param1=100,param2=70,minRadius=50,maxRadius=200)
        if np.any(circles==None):
            print 'no'
        else:
            circles = np.uint16(np.around(circles))
            yellow=0
            for i in circles[0,:]:
                cv2.circle(frame0,(i[0],i[1]),i[2],(255,255,255),2)
                cv2.circle(frame0,(i[0],i[1]),2,(255,255,255),3)
                for j in range(0,10):
                    for k in range(0,10):
                        (b,g,r)=frame0[np.uint16(i[1])-10+j,np.uint16(i[0])-10+k]
                        if g>127 and g-b>60:
                            yellow +=1
            if yellow>=50:
                print 'True'
    elif color == 'purple':
        circles = cv2.HoughCircles(sub3,cv2.HOUGH_GRADIENT,2,200,param1=100,param2=60,minRadius=50,maxRadius=200)
        if np.any(circles==None):
            print 'no'
        else:
            circles = np.uint16(np.around(circles))
            purple=0
            for i in circles[0,:]:
                cv2.circle(frame0,(i[0],i[1]),i[2],(255,255,255),2)
                cv2.circle(frame0,(i[0],i[1]),2,(255,255,255),3)
                for j in range(0,10):
                    for k in range(0,10):
                        (b,g,r)=frame0[np.uint16(i[1])-5,np.uint16(i[0])-5]
                        if b-r<20 and r>50:
                            purple +=1
            if purple>=50:
                print 'True'
                    
#    cv2.imshow('R-B',sub1)
#    cv2.imshow('R-G',sub2)
#    cv2.imshow('B-G',sub3)
#    cv2.imshow('B-R',sub4)
#    cv2.imshow('G-R',sub5)
#    cv2.imshow('G-B',sub6)
    cv2.imshow('detect',frame0)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cp0.release()
    e=t.time()
#    print e-s
cv2.waitKey(1)


