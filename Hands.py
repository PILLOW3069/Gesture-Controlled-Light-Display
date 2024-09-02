import mediapipe
import cv2
import numpy
import math

class Hand:
    def __init__(self,mode=False,maxh=1,complex=1,det_conf=.9,trac_conf=.9):
        self.hands=mediapipe.solutions.hands.Hands(mode,maxh,complex,det_conf,trac_conf)
        self.pen=mediapipe.solutions.drawing_utils
        self.results=None
        self.line_dist=0

    def get_hand(self,img):
            _img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            self.results=self.hands.process(_img)
            # if self.results.multi_hand_landmarks:
            #     for i in self.results.multi_hand_landmarks:
            #         self.pen.draw_landmarks(img,i,mediapipe.solutions.hands.HAND_CONNECTIONS)
            return img
    
    def get_finger(self,img,finger=""):
        positions=[]
        if finger=="thumb":
            points=[2,3,4]
        elif finger=="index":
             points=[5,6,7,8]
        elif finger=="middle":
             points=[9,10,11,12]
        elif finger=="ring":
             points=[13,14,15,16]
        elif finger=="pinky":
             points=[17,18,19,20]
        else:
             return [self.get_finger(img,"thumb"),self.get_finger(img,"index"),self.get_finger(img,"middle"),self.get_finger(img,"ring"),self.get_finger(img,"pinky")]
        if not self.results:
             self.get_hands(img)
        if self.results.multi_hand_landmarks:
             h,w=img.shape[:2]
             for i in self.results.multi_hand_landmarks:
                    for point,landmark in enumerate(i.landmark):
                         if point in points:
                                positions.append((int(landmark.x*w),int(landmark.y*h)))
        if positions:
             return positions

    def finger_count(self,img):
        mapping={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE"}
        count=0
        points=self.get_finger(img)
        if points:
            if points[0] or points[1] or points[2] or points[3] or points[4] :
                if points[1][-1][0]>points[1][-2][0]:
                    count+=1
                if points[2][-1][0]>points[2][-2][0]:
                    count+= 1
                if points[3][-1][0]>points[3][-2][0]:
                    count+= 1
                if points[4][-1][0]>points[4][-2][0]:
                    count+= 1
                if points[0][-1][0]>points[0][-2][0]:
                     count+= 1
        return mapping[count]
    def draw_line(self,img,finger1="thumb",finger2="index",draw=False):
         if not self.results:
                self.get_hands(img)
         if self.results.multi_hand_landmarks:
                for i in self.results.multi_hand_landmarks:
                    fing1_pos=self.get_finger(img,finger1)[-1] if self.get_finger(img,finger1) else None
                    fing2_pos=self.get_finger(img,finger2)[-1] if self.get_finger(img,finger2) else None
                    if fing1_pos and fing2_pos:
                        self.line_dist=math.hypot(fing1_pos[0]-fing2_pos[0],fing1_pos[1]-fing2_pos[1])
                        if draw:
                            cv2.line(img,fing1_pos,fing2_pos,(0,255,0),5)
                            return img
                        return [fing1_pos,(fing1_pos[0]+fing2_pos[0]//2,fing1_pos[1]+fing2_pos[1]//2),fing2_pos],math.hypot(fing1_pos[0]-fing2_pos[0],fing1_pos[1]-fing2_pos[1])
         return None,None
    

def map_distance_to_scale(distance,min_distance=15,max_distance=200):

    mapping={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE"}
    return mapping[int(numpy.interp(distance,[min_distance,max_distance],[0,5]))]

if __name__=="__main__":
    camera=cv2.VideoCapture(0)
    detector=Hand()
    while True:
        idk,img=camera.read()
        detector.get_hand(img)
        detector.draw_line(img,draw=True)
        #print(detector.line_dist)
        print(map_distance_to_scale(detector.line_dist))
        cv2.imshow("Camera",img)
        cv2.waitKey(1)