import cv2
from background import calc_accum_avg
from segmentation import segment
from finger_counter import count_fingers

roi_top = 20
roi_bottom = 300
roi_right = 300
roi_left = 600

accumulated_weight = 0.5

cam = cv2.VideoCapture(0)
num_frames = 0

while True:

    ret, frame = cam.read()

    frame = cv2.flip(frame,1)
    frame_copy = frame.copy()

    roi = frame[roi_top:roi_bottom, roi_right:roi_left]

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(7,7),0)

    if num_frames < 150:

        calc_accum_avg(gray, accumulated_weight)

        cv2.putText(frame_copy,"Calibrating Background",
        (200,400), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    else:

        hand = segment(gray)

        if hand is not None:

            thresholded, hand_segment = hand

            fingers = count_fingers(thresholded, hand_segment)

            cv2.putText(frame_copy,str(fingers),
            (70,45),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

            cv2.imshow("Thresholded", thresholded)

    cv2.rectangle(frame_copy,(roi_left,roi_top),(roi_right,roi_bottom),(0,0,255),5)

    num_frames += 1

    cv2.imshow("Finger Counter", frame_copy)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()