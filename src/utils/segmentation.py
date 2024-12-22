import cv2
import numpy as np
from ..core.exceptions import ImageProcessingError


def segment_skin(lab_image: np.ndarray) -> np.ndarray:
    """
    Segment skin regions from the LAB color space image.

    Args:
        lab_image (np.ndarray): Input image in LAB color space

    Returns:
        np.ndarray: Binary mask of skin regions
    """
    lower_skin = np.array([20, 130, 130])
    upper_skin = np.array([255, 180, 180])
    mask = cv2.inRange(lab_image, lower_skin, upper_skin)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)
    return mask


def segment_hair(lab_image: np.ndarray) -> np.ndarray:
    """
    Segment hair regions from the LAB color space image.

    Args:
        lab_image (np.ndarray): Input image in LAB color space

    Returns:
        np.ndarray: Binary mask of hair regions
    """
    l_channel = lab_image[:, :, 0]
    _, hair_mask = cv2.threshold(l_channel, 50, 255, cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    hair_mask = cv2.erode(hair_mask, kernel, iterations=1)
    hair_mask = cv2.dilate(hair_mask, kernel, iterations=1)
    return hair_mask


def segment_eyes(lab_image: np.ndarray) -> np.ndarray:
    """
    Segment eye regions using Haar cascade classifier.

    Args:
        lab_image (np.ndarray): Input image in LAB color space

    Returns:
        np.ndarray: Binary mask of eye regions

    Raises:
        ImageProcessingError: If eye cascade classifier cannot be loaded
    """
    try:
        # Convert to grayscale for eye detection
        gray = cv2.cvtColor(
            cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR), cv2.COLOR_BGR2GRAY
        )

        # Load the eye cascade classifier
        cascade_path = cv2.data.haarcascades + "haarcascade_eye.xml"
        eye_cascade = cv2.CascadeClassifier(cascade_path)

        if eye_cascade.empty():
            raise ImageProcessingError("Failed to load eye cascade classifier")

        # Detect eyes
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        # Create mask
        mask = np.zeros(gray.shape, dtype=np.uint8)

        # If no eyes detected, return empty mask
        if len(eyes) == 0:
            return mask

        # Draw detected eye regions on mask
        for x, y, w, h in eyes:
            cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 255, 255), -1)

        return mask

    except Exception as e:
        raise ImageProcessingError(f"Eye detection failed: {str(e)}")
