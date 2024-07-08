import cv2
import numpy as np

def segment_skin(lab_image):
    lower_skin = np.array([20, 130, 130])
    upper_skin = np.array([255, 180, 180])
    mask = cv2.inRange(lab_image, lower_skin, upper_skin)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)
    return mask

def segment_hair(lab_image):
    l_channel = lab_image[:,:,0]
    _, hair_mask = cv2.threshold(l_channel, 50, 255, cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    hair_mask = cv2.erode(hair_mask, kernel, iterations=1)
    hair_mask = cv2.dilate(hair_mask, kernel, iterations=1)
    return hair_mask

def segment_eyes(lab_image):
    gray = cv2.cvtColor(cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR), cv2.COLOR_BGR2GRAY)
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    mask = np.zeros(gray.shape, dtype=np.uint8)
    for (x, y, w, h) in eyes:
        cv2.rectangle(mask, (x, y), (x+w, y+h), (255, 255, 255), -1)
    return mask