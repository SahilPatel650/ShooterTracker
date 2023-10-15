import cv2
from transformers import BlipProcessor, BlipForQuestionAnswering

def initialize_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
    model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")
    return processor, model

def inference(img, question, processor, model, isUrl=False):
    inputs = processor(img, question, return_tensors="pt")
    out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True).strip()

def get_description_cropped(img, processor, model):
    out = ""
    shirt_color = inference(img, "What color is the person's shirt?", processor ,model)
    shirt_pattern = inference(img, "Describe the pattern on the person's shirt?", processor, model)
    shirt_desc = f"{shirt_color}, {shirt_pattern}"
    out += "\nshirt: " + shirt_desc
    has_hat = inference(img, "Is the person wearing a hat or cap?", processor, model)
    print(has_hat)
    if has_hat.lower() == "yes" or has_hat.lower() == "hat" or has_hat.lower() == "cap":
        hat_desc = inference(img, "What color is the hat?", processor, model)
    else:
        hat_desc = "N/A"
    out += "\nhat: " + hat_desc
    ethnicity_desc = inference(img, "What ethnicity is the person?", processor, model)
    out += "\nethinicity: " + ethnicity_desc
    return out

def get_description(img_path, top_left, bottom_right, processor, model):
    img = cv2.imread(img_path)
    img = img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    return get_description_cropped(img, processor,  model)
