# Image Question Answering with BLIP2

This Python script uses the BLIP2 (Bidirectional Language-Image Pretraining) model from Salesforce to perform image question answering. Users can input an image and ask questions about it, and the model will generate an answer.

## Requirements

- Python 3.7 or later
- PyTorch
- Transformers library
- Pillow (PIL)

You can install the required packages using pip:

## Usage

1. Place the image you want to use in the same directory as the `model.py` file, and name it `image.png`.
2. Run the `model.py` script:
3. The script will prompt you to ask a question about the image. Type your question and press Enter.
4. The model will generate an answer and print it to the console.
5. To exit the question-answering loop, type "exit" and press Enter.

## How it Works

The script uses the pre-trained BLIP2 model from Salesforce to perform image question answering. The model is loaded from the Hugging Face Transformers library, and the `AutoProcessor` class is used to preprocess the input image and question.

The script enters a loop where it prompts the user to ask a question, then passes the image and question to the BLIP2 model to generate an answer. The generated answer is then printed to the console.

## Limitations

- The script currently only supports a single image, which must be named `image.png` and placed in the same directory as the `model.py` file.
- The model has a limited ability to answer questions, and its performance may vary depending on the complexity of the question and the content of the image.

## License

This project is licensed under the [MIT License](LICENSE).
