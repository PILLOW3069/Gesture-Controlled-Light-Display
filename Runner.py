from Hands import Hand,map_distance_to_scale
import cv2
import serial
import serial.tools.list_ports as sp
import time
import threading

def runner():
    ports=sp.comports()
    serial_=serial.Serial()
    a=[]
    for i in ports:
        a.append(str(i))
    print(a)
    com=input("select com : ")
    for i in a:
        if i.startswith("COM"+str(com)):
            use="COM"+str(com)
    serial_.baudrate=9600
    print(use)
    serial_.port=use
    serial_.open()
    camera=cv2.VideoCapture(0)
    detector=Hand(trac_conf=.9,det_conf=.9)
    temp=""
    while True:
        idk,img=camera.read()
        detector.get_hand(img)
        detector.draw_line(img,draw=True)
        data=str((map_distance_to_scale(detector.line_dist)))+"\n"
        if data!=temp:
            serial_.write(data.encode('utf-8'))
            print(data)
            temp=data
        cv2.imshow("camera",img)
        cv2.waitKey(1)
        time.sleep(1/24)

if __name__=="__main__":
    runner()