from huggingface_hub import InferenceClient
from PIL import Image
import sys
import os
from datetime import datetime

# Hugging Face API token
HUGGING_FACE_TOKEN = "**************************"  # Replace with your actual token

# Ensure 'generated' directory exists
GENERATED_DIR = "generated"
os.makedirs(GENERATED_DIR, exist_ok=True)

def generate_image(prompt):
    try:
        # Initialize the client
        client = InferenceClient(
            model="Artples/LAI-ImageGeneration-vSDXL-2",
            token=HUGGING_FACE_TOKEN
        )

        # Generate the image
        print("Generating image...", file=sys.stderr)
        image = client.text_to_image(prompt)

        # Create unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_filename = f"generated_image_{timestamp}.png"
        
        # Save the image
        save_path = os.path.join(GENERATED_DIR, image_filename)
        image.save(save_path)

        # Print only the filename (important for Node.js to capture it)
        print(image_filename)
        return True
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No prompt provided", file=sys.stderr)
        sys.exit(1)
    
    prompt = sys.argv[1]
    success = generate_image(prompt)
    if not success:
        sys.exit(1)