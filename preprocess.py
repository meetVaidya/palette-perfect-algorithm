import cv2
import numpy as np

def preprocess_image(image, target_size=(300, 300)):
    # Resize the image
    resized = cv2.resize(image, target_size)
    
    # Apply Gaussian blur for noise reduction
    blurred = cv2.GaussianBlur(resized, (5, 5), 0)
    
    # Convert to LAB color space
    lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
    
    return lab