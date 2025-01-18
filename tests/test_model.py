import unittest
import numpy as np
from model.kanvas_model import KanvasModel

class TestKanvasModel(unittest.TestCase):
    def setUp(self):
        config = {
            'model_type': 'tensorflow',  # Or 'torch' based on your setup
            'model_path': 'models/kanvas_model_v1.h5',
        }
        self.model = KanvasModel(config)
        
    def test_model_loading(self):
        """Test if the model loads correctly."""
        self.assertIsNotNone(self.model.model, "Model failed to load.")

    def test_generate_media(self):
        """Test the generate_media function."""
        input_data = np.zeros((256, 256, 3))  # Example of dummy image data
        result = self.model.generate_media(input_data)
        self.assertIsInstance(result, np.ndarray, "Generated media is not a valid format.")

if __name__ == "__main__":
    unittest.main()
