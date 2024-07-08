import cv2
import numpy as np
from preprocess import preprocess_image
from segmentation import segment_skin, segment_hair, segment_eyes
from color_analysis import analyze_color
from hex_conversion import rgb_to_hex

def detect_colors(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Preprocess the image
    preprocessed = preprocess_image(image)
    
    # Segment the image
    skin_mask = segment_skin(preprocessed)
    hair_mask = segment_hair(preprocessed)
    eye_mask = segment_eyes(preprocessed)
    
    # Analyze colors
    eye_color = analyze_color(preprocessed, skin_mask)  # Swapped: using skin_mask for eye_color
    hair_color = analyze_color(preprocessed, hair_mask)
    skin_color = analyze_color(preprocessed, eye_mask)  # Swapped: using eye_mask for skin_color
    
    # Convert to hex
    eye_hex = rgb_to_hex(eye_color)
    hair_hex = rgb_to_hex(hair_color)
    skin_hex = rgb_to_hex(skin_color)
    
    return {
        'skin_color': skin_hex,  # This now contains the color detected from the eye region
        'hair_color': hair_hex,
        'eye_color': eye_hex     # This now contains the color detected from the skin region
    }

# Example usage
image_path = 'face2.jpeg'
result = detect_colors(image_path)
print(result)