import cv2
import numpy as np

def analyze_color(image, mask):
    # Apply the mask to the image
    masked = cv2.bitwise_and(image, image, mask=mask)
    
    # Convert back to BGR color space
    bgr = cv2.cvtColor(masked, cv2.COLOR_LAB2BGR)
    
    # Calculate the average color of the masked region
    average_color = cv2.mean(bgr, mask=mask)[:3]
    
    return average_color