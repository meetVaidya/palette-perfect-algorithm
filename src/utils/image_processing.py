from typing import Tuple
import cv2
import numpy as np
from ..core.exceptions import ImageProcessingError


def load_image(image_path: str) -> np.ndarray:
    """
    Load and validate an image from the given path.

    Args:
        image_path (str): Path to the image file

    Returns:
        np.ndarray: Loaded image in BGR format

    Raises:
        ImageProcessingError: If the image cannot be loaded
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ImageProcessingError(f"Failed to load image: {image_path}")
    return image


def preprocess_image(
    image: np.ndarray, target_size: Tuple[int, int] = (300, 300)
) -> np.ndarray:
    """
    Preprocess the input image for color detection.

    Args:
        image (np.ndarray): Input image in BGR format
        target_size (tuple): Target size for resizing

    Returns:
        np.ndarray: Preprocessed image in LAB color space
    """
    resized = cv2.resize(image, target_size)
    blurred = cv2.GaussianBlur(resized, (5, 5), 0)
    return cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
