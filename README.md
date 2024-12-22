# Palette Perfect Algorithm

A Python-based facial feature color detection system that analyzes images to extract dominant colors from skin, hair, and eyes. This tool uses computer vision techniques to automatically detect and analyze different facial features and return their corresponding color values in hex format.

## 🎯 Features

- Automated detection of facial features (skin, hair, eyes)
- Color analysis in LAB color space for accurate color representation
- Hex color code output for easy integration with design tools
- Robust error handling and input validation
- Modular and extensible architecture

## 🛠️ Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher
- pip (Python package installer)
- OpenCV system dependencies (if on Linux)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/meetVaidya/palette-perfect-algorithm.git
cd palette-perfect-algorithm
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 📁 Project Structure

```
palette_perfect_algorithm/
├── src/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── color_detector.py
│   │   └── exceptions.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── image_processing.py
│   │   ├── color_analysis.py
│   │   ├── segmentation.py
│   │   └── validators.py
│   └── config/
│       ├── __init__.py
│       └── settings.py
├── tests/
│   └── __init__.py
├── requirements.txt
├── main.py
└── README.md
```

## 🚀 Usage

### Basic Usage

```python
from src.core.color_detector import detect_facial_colors

# Analyze an image
try:
    colors = detect_facial_colors("path/to/your/image.jpg")
    print(colors)
except Exception as e:
    print(f"Error: {str(e)}")
```

### Example Output

```python
{
    'skin_color': '#F5D2B3',
    'hair_color': '#2C1810',
    'eye_color': '#634E3F'
}
```

## ⚙️ Configuration

The project uses several configuration parameters that can be adjusted in `src/config/settings.py`:

- Image preprocessing parameters
- Color detection thresholds
- Segmentation settings

## 📋 Dependencies

Main dependencies include:

```
opencv-python>=4.10.0
numpy>=1.21.0
```

For a complete list of dependencies, see `requirements.txt`.

## 🔍 API Reference

### Core Functions

#### `detect_facial_colors(image_path: str) -> Dict[str, str]`
Analyzes an image and returns detected colors for facial features.

Parameters:
- `image_path`: Path to the input image file

Returns:
- Dictionary containing hex color codes for skin, hair, and eyes

### Utility Functions

#### `preprocess_image(image: np.ndarray, target_size: Tuple[int, int] = (300, 300)) -> np.ndarray`
Preprocesses the input image for analysis.

#### `analyze_color(image: np.ndarray, mask: np.ndarray) -> Tuple[float, float, float]`
Analyzes color in a masked region of an image.

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make changes and commit (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## ⚠️ Known Issues

- Eye detection may be less accurate in poor lighting conditions
- Hair segmentation might include background elements in some cases
- Performance may vary with different image resolutions
