#  AI Image Captioning – CodSoft AI Internship (Task 3)

##  Project Overview
This project implements an **AI-powered Image Captioning System** that combines **Computer Vision** and **Natural Language Processing** to automatically generate meaningful, context-aware descriptions for images.  
It uses the **Google Generative AI (Gemini 1.5 Flash)** model for visual understanding and language generation.

##  Features
- Extracts **visual details, text, and tables** from images  
- Generates **fluent, context-aware captions**  
- Supports **single or multiple images** in one run  
- Easy to integrate into accessibility tools, content automation, and document analysis  

##  Tech Stack
- **Language:** Python  
- **AI Model:** Google Generative AI – Gemini 1.5 Flash  
- **Environment:** Google Colab / VS Code  
- **Libraries:**  
  - `google-generativeai`  
  - `os`  
  - `dotenv` (optional for API key handling)

##  Project Structure
```

 Image-Captioning
│──  image\_captioning.py     # Main Python script
│──  requirements.txt        # Required dependencies
│──  README.md               # Project documentation
│──  sample\_images           # Sample input images
│──  outputs                 # Generated captions

````

---

## ⚙️ Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/Image-Captioning.git
   cd Image-Captioning
````

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Google Generative AI API Key**

   * Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   * Set it in your environment:

     ```bash
     export GOOGLE_API_KEY="your_api_key_here"
     ```



##  Usage

python
from image_captioning import get_image_summaries

image_list = ["sample_images/img1.jpg", "sample_images/img2.jpg"]
captions = get_image_summaries(image_list)

for idx, caption in enumerate(captions, start=1):
    print(f"Image {idx} Caption: {caption}")


## Example Output

**Input:**  `beach.jpg`
**Output:** `"A serene beach with golden sand, gentle waves, and a vibrant sunset in the background."`




