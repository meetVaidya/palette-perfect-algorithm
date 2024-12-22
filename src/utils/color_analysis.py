from typing import Tuple
import cv2
import numpy as np


def analyze_color(image: np.ndarray, mask: np.ndarray) -> Tuple[float, float, float]:
    """
    Analyze the dominant color in the masked region of an image.

    Args:
        image (np.ndarray): Input image in LAB color space
        mask (np.ndarray): Binary mask for the region of interest

    Returns:
        tuple: Average BGR color values
    """
    masked = cv2.bitwise_and(image, image, mask=mask)
    bgr = cv2.cvtColor(masked, cv2.COLOR_LAB2BGR)
    mean_values = cv2.mean(bgr, mask=mask)
    return (mean_values[0], mean_values[1], mean_values[2])


def rgb_to_hex(rgb: Tuple[float, float, float]) -> str:
    """
    Convert RGB color values to hexadecimal format.

    Args:
        rgb (tuple): RGB color values

    Returns:
        str: Color in hexadecimal format
    """
    return "#{:02x}{:02x}{:02x}".format(int(rgb[2]), int(rgb[1]), int(rgb[0]))
