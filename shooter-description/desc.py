import requests
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering

def initialize_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
    model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")
    return processor, model

def inference(img, question, processor, model, isUrl=False):
    raw_image = Image.open(requests.get(img, stream=True).raw if isUrl else img)
    raw_image = raw_image.convert('RGB')
    inputs = processor(raw_image, question, return_tensors="pt")
    out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True).strip()

def get_description(img, processor, model):
    out = ""
    shirt_desc = inference(img, "Describe the person's shirt.", processor,model)
    out += "\nshirt: " + shirt_desc
    hat_desc = inference(img, "Is the person wearing a hat? If so, what color?", processor, model)
    out += "\nhat: " + hat_desc
    ethnicity_desc = inference(img, "What ethnicity is the person?", processor, model)
    out += "\nethinicity: " + ethnicity_desc
    gen_desc= inference(img, "Describe the person.", processor, model)
    out += "\ngeneral features: " + gen_desc
    return out

if __name__ == "__main__":
    processor, model = initialize_model()
    desc = get_description("~/Desktop/shooter.jpeg", processor, model)
    print(desc)
