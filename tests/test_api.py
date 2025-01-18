import unittest
import json
from api.api_handler import ApiHandler
from model.kanvas_model import KanvasModel
from flask.testing import FlaskClient

class TestApiHandler(unittest.TestCase):
    def setUp(self):
        # Setup the Kanvas model for testing
        config = {
            'model_type': 'tensorflow',  # Or 'torch' based on your setup
            'model_path': 'models/kanvas_model_v1.h5',
        }
        self.model = KanvasModel(config)
        self.api_handler = ApiHandler(self.model)
        self.client = self.api_handler.app.test_client()

    def test_generate_media_api(self):
        """Test the /generate_media endpoint."""
        input_data = {'input_data': 'dummy_image_data'}  # Use actual test data
        response = self.client.post('/generate_media', data=json.dumps(input_data), content_type='application/json')
        self.assertEqual(response.status_code, 200, "API call failed.")
        self.assertIn('generated_media', json.loads(response.data), "Response did not contain expected media data.")

if __name__ == "__main__":
    unittest.main()
