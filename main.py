from src.core.exceptions import ImageProcessingError


def main():
    try:
        from src.core.color_detector import detect_facial_colors

        image_path = "data/face2.jpeg"
        colors = detect_facial_colors(image_path)
        print("Detected colors:")
        print(f"Skin: {colors['skin_color']}")
        print(f"Hair: {colors['hair_color']}")
        print(f"Eyes: {colors['eye_color']}")
    except ImageProcessingError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    main()
