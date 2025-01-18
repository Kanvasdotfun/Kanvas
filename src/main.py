import os
from src.model.kanvas_model import KanvasModel
from src.api.api_handler import APIHandler

def main():
    print("Starting Kanvas AI Media Generation...")
    
    # Load the AI model
    model = KanvasModel()

    # Initialize API handler
    api = APIHandler()

    # Example of using the API to create content
    result = api.generate_media("Generate a futuristic city with neon lights.")
    
    # Output the result
    print(f"Generated Media: {result}")

if __name__ == "__main__":
    main()
