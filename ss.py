import google.generativeai as genai
import os

# API configuration
api_key = "YOUR_API_KEY_HERE"  # <-- Replace with your API key
genai.configure(api_key=api_key)

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Function to get captions for images
def get_image_summaries(image_paths):
    model = genai.GenerativeModel("gemini-1.5-flash")
    summaries = []

    for path in image_paths:
        with open(path, "rb") as img_file:
            image_data = img_file.read()

        response = model.generate_content([
            {"mime_type": "image/jpeg", "data": image_data},
            "Describe the contents of this image. Focus on any text, tables, or visual elements that can be used for question answering."
        ])
        summaries.append(response.text)

    return summaries

if __name__ == "__main__":
    image_list = ["/content/img.jpg"]  # You can add more image paths
    results = get_image_summaries(image_list)
    for idx, summary in enumerate(results, start=1):
        print(f"Image {idx} Summary:\n{summary}\n")
