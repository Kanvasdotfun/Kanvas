from flask import Flask, jsonify, request
from model.kanvas_model import KanvasModel

class ApiHandler:
    def __init__(self, model: KanvasModel):
        self.model = model
        self.app = Flask(__name__)
        self._setup_routes()

    def _setup_routes(self):
        self.app.add_url_rule('/generate_media', 'generate_media', self.generate_media, methods=['POST'])

    def generate_media(self):
        data = request.get_json()

        # Assuming input_data is in the form of a base64-encoded image or text
        input_data = data['input_data']
        
        # Generate media through the Kanvas model
        generated_media = self.model.generate_media(input_data)

        # Convert generated media to a format (e.g., base64 or file)
        response = self._convert_media_to_response_format(generated_media)
        
        return jsonify({'generated_media': response}), 200

    def _convert_media_to_response_format(self, generated_media):
        """
        Convert generated media to a format suitable for sending back via API.
        """
        # In a real implementation, this could convert an image into base64 encoding
        return generated_media

    def run(self):
        self.app.run(debug=True)
