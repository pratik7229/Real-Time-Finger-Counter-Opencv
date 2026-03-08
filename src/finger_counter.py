import cv2
import numpy as np

def count_fingers(thresholded, hand_segment):

    conv_hull = cv2.convexHull(hand_segment)

    top = tuple(conv_hull[conv_hull[:,:,1].argmin()][0])
    bottom = tuple(conv_hull[conv_hull[:,:,1].argmax()][0])
    left = tuple(conv_hull[conv_hull[:,:,0].argmin()][0])
    right = tuple(conv_hull[conv_hull[:,:,0].argmax()][0])

    cX = (left[0] + right[0]) // 2
    cY = (top[1] + bottom[1]) // 2

    distance = max(
        np.linalg.norm(np.array([cX,cY]) - np.array(left)),
        np.linalg.norm(np.array([cX,cY]) - np.array(right)),
        np.linalg.norm(np.array([cX,cY]) - np.array(top)),
        np.linalg.norm(np.array([cX,cY]) - np.array(bottom))
    )

    radius = int(0.8 * distance)

    circumference = (2 * np.pi * radius)

    circular_roi = np.zeros(thresholded.shape[:2], dtype="uint8")

    cv2.circle(circular_roi, (cX, cY), radius, 255, 1)

    circular_roi = cv2.bitwise_and(thresholded, thresholded, mask=circular_roi)

    contours, _ = cv2.findContours(
        circular_roi.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_NONE
    )

    count = 0

    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)

        if (cY + (cY * 0.25)) > (y + h) and contour.shape[0] < circumference * 0.25:
            count += 1

    return count