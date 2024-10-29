Image Question-Answering System using BLIP-2
This repository hosts an interactive question-answering system that uses the BLIP-2 (Bootstrapping Language-Image Pre-training) model from Hugging Face to answer questions based on image content. By loading an image and entering a question, users can get AI-generated responses that analyze and describe elements of the image.

Model Overview
This project uses the BLIP-2 (Bootstrapping Language-Image Pre-training) model, specifically Salesforce/blip2-opt-2.7b, from Hugging Face. BLIP-2 combines vision and language pre-training, enabling the model to understand and generate text responses relevant to the visual content of an image.

Features
Image Processing: Loads an image and processes it with the BLIP-2 model for contextual question answering.
Interactive Q&A: Users can ask multiple questions about an image within a single session, making the application highly interactive.
Efficient GPU Utilization: Automatically detects GPU availability and uses it to accelerate processing if available.
Setup Instructions
1. Clone the Repository
First, clone this repository to your local machine:

bash
Copy code
git clone https://github.com/Veer-w/image-question-answering-blip2.git
cd image-question-answering-blip2
2. Install Dependencies
Create a virtual environment (optional but recommended) and install dependencies from the requirements.txt file:

bash
Copy code
# Create virtual environment
python -m venv venv
source venv/bin/activate      # For MacOS/Linux
venv\Scripts\activate         # For Windows

# Install dependencies
pip install -r requirements.txt
3. Download the Model
The Salesforce/blip2-opt-2.7b model will automatically download when you run the code, as it’s pulled from Hugging Face’s model repository.

4. Run the Code
Place your target image (e.g., image.png) in the project folder, and execute the script:

bash
Copy code
python main.py
Usage
Load the Image: Make sure image.png is in the directory or specify another image in the code.
Ask Questions: The program will prompt you to type a question about the image. Type your question and hit Enter.
Exit: Type "exit" when you’re done to terminate the session.
File Structure
main.py: The main script for loading the image and running the Q&A loop.
requirements.txt: Lists all the dependencies required for this project.
README.md: Project description and setup instructions.
Example Interaction
When running the code, the console interaction would look like:

plaintext
Copy code
Ask a question about the image (or type 'exit' to quit): What is in the image?
Answer: "A dog sitting in a park."

Ask a question about the image (or type 'exit' to quit): What color is the dog?
Answer: "The dog is brown and white."

Ask a question about the image (or type 'exit' to quit): exit
Exiting the question loop.
Requirements
Dependencies are specified in the requirements.txt file:

plaintext
Copy code
torch==2.0.0
transformers==4.30.0
Pillow==9.5.0
Model and Libraries
Transformers: The transformers library provides the AutoProcessor and Blip2ForConditionalGeneration modules, which allow seamless integration with Hugging Face models.
Torch: Used for deep learning computations, allowing for efficient model execution, especially on GPU.
Pillow: A library for image processing, used here to load images.
Acknowledgements
Salesforce Research: For developing the BLIP-2 model architecture.
Hugging Face: For hosting pre-trained models and providing the transformers library, which simplifies model deployment.
