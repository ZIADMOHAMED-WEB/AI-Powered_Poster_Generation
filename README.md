# 🖼️ Text-to-Image Generation using Hugging Face Inference API

This project generates high-quality images from text prompts using the [`Artples/LAI-ImageGeneration-vSDXL-2`](https://huggingface.co/Artples/LAI-ImageGeneration-vSDXL-2) model on Hugging Face. It saves the images locally with timestamped filenames.

---

## 🚀 Features

- Uses the Hugging Face **Inference API** to generate images from prompts
- Automatically saves generated images to a `generated/` folder
- Prints only the filename of the generated image (useful for integration with Node.js or other tools)

---

## 📦 Requirements

Install the required Python packages:

```bash
pip install huggingface_hub pillow
🔑 Setup
Get a Hugging Face API Token:

Visit https://huggingface.co/settings/tokens

Generate a new token with access to inference

Edit the Script:

Replace this line with your actual Hugging Face token:

python
Copy
Edit
HUGGING_FACE_TOKEN = "**************************"
📂 Folder Structure
pgsql
Copy
Edit
project-root/
├── generate_image.py
├── generated/             ← Output images saved here
└── README.md
🧪 Usage
Run the script from the command line and provide a text prompt:

bash
Copy
Edit
python generate_image.py "A futuristic city in the clouds during sunset"
The script will:

Generate an image

Save it as generated/generated_image_<timestamp>.png

Print the filename to stdout

🧠 Notes
If no prompt is provided, the script will print an error and exit.

Error messages and status updates are printed to stderr.

Filenames are timestamped to avoid collisions.

🔗 Model Info
Model: Artples/LAI-ImageGeneration-vSDXL-2

Backend: Hugging Face Inference API

📄 License
This script is provided under the MIT License. The image model used may have its own licensing and usage restrictions. Always check the model card on Hugging Face.

✨ Example
bash
Copy
Edit
$ python generate_image.py "A mystical forest with glowing trees"
Generating image...
generated_image_20250510_194533.png
The generated image will be saved in the generated/ directory.

yaml
Copy
Edit
