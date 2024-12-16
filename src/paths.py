from pathlib import Path

# Get repo root directory
REPO_ROOT = Path(__file__).parent.parent

# Data directories
DATA_DIR = REPO_ROOT / "data"
IMAGES_DIR = DATA_DIR / "images"
MODELS_DIR = DATA_DIR / "models"

# Image subdirectories
CLASSIFICATION_IMAGES = IMAGES_DIR / "image_classification"
DETECTION_IMAGES = IMAGES_DIR / "object_detection"
SEGMENTATION_IMAGES = IMAGES_DIR / "semantic_segmentation"
TRACKING_VIDEOS = IMAGES_DIR / "object_tracking"

# Output directory
OUTPUTS_DIR = REPO_ROOT / "outputs"

# Create directories if they don't exist
for dir_path in [
    CLASSIFICATION_IMAGES,
    DETECTION_IMAGES,
    SEGMENTATION_IMAGES,
    MODELS_DIR,
    OUTPUTS_DIR,
]:
    dir_path.mkdir(parents=True, exist_ok=True)
