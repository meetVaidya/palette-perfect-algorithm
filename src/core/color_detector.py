from typing import Dict
from ..utils.image_processing import load_image, preprocess_image
from ..utils.color_analysis import analyze_color, rgb_to_hex
from ..utils.validators import validate_image_path
from ..utils.segmentation import segment_skin, segment_hair, segment_eyes
from .exceptions import ImageProcessingError


def detect_facial_colors(image_path: str) -> Dict[str, str]:
    """
    Detect dominant colors in facial features (skin, hair, and eyes).

    Args:
        image_path (str): Path to the input image

    Returns:
        dict: Dictionary containing hex color codes for skin, hair, and eyes

    Raises:
        InvalidImageError: If the image is invalid or cannot be processed
        ImageProcessingError: If color detection fails
    """
    try:
        # Validate image path
        validate_image_path(image_path)

        # Load and preprocess image
        image = load_image(image_path)
        preprocessed = preprocess_image(image)

        # Segment facial features
        skin_mask = segment_skin(preprocessed)
        hair_mask = segment_hair(preprocessed)
        eye_mask = segment_eyes(preprocessed)

        # Analyze colors
        skin_color = analyze_color(preprocessed, skin_mask)
        hair_color = analyze_color(preprocessed, hair_mask)
        eye_color = analyze_color(preprocessed, eye_mask)

        # Convert to hex format
        return {
            "skin_color": rgb_to_hex(skin_color),
            "hair_color": rgb_to_hex(hair_color),
            "eye_color": rgb_to_hex(eye_color),
        }

    except Exception as e:
        raise ImageProcessingError(f"Color detection failed: {str(e)}")
