import numpy as np

def normalize_image(image: np.ndarray):
    """
    Normalize the image data to ensure it fits the expected input range of the model.
    """
    return image / 255.0

def resize_image(image: np.ndarray, target_size=(256, 256)):
    """
    Resize the image to the required size for processing.
    """
    return np.resize(image, target_size)
