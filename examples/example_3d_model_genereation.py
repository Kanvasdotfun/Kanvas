import json
from kanvas.model import generate_3d_model

# Example input for 3D model generation
model_input = {
    "description": "Futuristic vehicle design with smooth curves and angular elements."
}

# Generate the 3D model
output_model = generate_3d_model(model_input)

# Display model URL or details
print("Generated 3D Model:", output_model)
