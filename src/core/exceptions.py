class ImageProcessingError(Exception):
    """Base exception for image processing errors."""

    pass


class InvalidImageError(ImageProcessingError):
    """Raised when the image is invalid or cannot be processed."""

    pass
