import os

from ..core.exceptions import InvalidImageError


def validate_image_path(image_path: str) -> None:
    """
    Validate if the image path exists and is a supported format.

    Args:
        image_path (str): Path to the image file

    Raises:
        InvalidImageError: If the image path is invalid or unsupported
    """
    if not os.path.exists(image_path):
        raise InvalidImageError(f"Image not found: {image_path}")

    supported_formats = [".jpg", ".jpeg", ".png", ".bmp"]
    if not any(image_path.lower().endswith(fmt) for fmt in supported_formats):
        raise InvalidImageError(
            f"Unsupported image format. Supported formats: {supported_formats}"
        )
