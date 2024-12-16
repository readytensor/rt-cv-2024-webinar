from pathlib import Path

# Get repo root directory
REPO_ROOT = Path(__file__).parent.parent

# Data directories
DATA_DIR = REPO_ROOT / "data"
VISUALS_DIR = DATA_DIR / "visuals"
MODELS_DIR = DATA_DIR / "models"

# Image subdirectories
CLASSIFICATION_IMAGES = VISUALS_DIR / "image_classification"
DETECTION_IMAGES = VISUALS_DIR / "object_detection"
SEGMENTATION_IMAGES = VISUALS_DIR / "semantic_segmentation"
TRACKING_VIDEOS = VISUALS_DIR / "object_tracking"

# Output directory
OUTPUTS_DIR = REPO_ROOT / DATA_DIR / "outputs"

# Create directories if they don't exist
for dir_path in [
    CLASSIFICATION_IMAGES,
    DETECTION_IMAGES,
    SEGMENTATION_IMAGES,
    MODELS_DIR,
    OUTPUTS_DIR,
]:
    dir_path.mkdir(parents=True, exist_ok=True)
