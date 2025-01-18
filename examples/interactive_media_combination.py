import json
from kanvas.model import combine_media

# Example input data for media combination
image_input = {
    "description": "A digital painting of a dragon in the sky."
}
audio_input = {
    "description": "Epic soundtrack accompanying a dragon flight."
}
model_input = {
    "description": "3D model of a flying dragon."
}

# Combine media types
final_output = combine_media(image_input, audio_input, model_input)

# Display the combined output
print("Combined Media Output:", final_output)
