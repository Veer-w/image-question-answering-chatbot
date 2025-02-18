from transformers import AutoProcessor, Blip2ForConditionalGeneration
import torch
from PIL import Image

processor = AutoProcessor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", torch_dtype=torch.float16)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

image = Image.open("add_your_image.png")  
while True:
    
    question = input("Ask a question about the image (or type 'exit' to quit): ")
    if question.lower() == 'exit':
        print("Exiting the question loop.")
        break
    
    prompt = f"Question: {question} Answer:"
    inputs = processor(image, text=prompt, return_tensors="pt").to(device)

    generated_ids = model.generate(**inputs, max_new_tokens=10)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

    print("Answer:", generated_text)
