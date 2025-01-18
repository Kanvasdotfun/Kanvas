import json
from kanvas.model import generate_audio

# Example input for audio generation
audio_input = {
    "description": "Relaxing ambient sounds of the ocean waves and birds."
}

# Generate the audio
output_audio = generate_audio(audio_input)

# Print the output audio URL
print("Generated Audio Output:", output_audio)
