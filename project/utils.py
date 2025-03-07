import random
import requests
from PIL import Image
from decouple import config
import google.api_core.exceptions
import google.generativeai as genai
from cloudinary.uploader import upload
from transformers import BlipProcessor, BlipForConditionalGeneration




def hash_generate(num_of_chars):
    """
    Generate a random string of numbers
    """
    return ''.join(random.choice('23456789') for x in range(num_of_chars))


def handle_image_upload(image_file):
    """
    Upload the image to Cloudinary if the environment 
    is production, else return the image
    """
    if config('ENV') == 'PROD':
        upload_result = upload(image_file)
        return upload_result['secure_url']
    else:
        return image_file


def generate_image_caption(image_url):
    """
    Generate a caption for the image using the Blip Image Captioning model
    """
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    if config('ENV') == 'PROD':
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        image = Image.open(response.raw)
    else:
        image = Image.open(image_url)

    inputs = processor(image, return_tensors="pt")
    caption = model.generate(**inputs)

    return processor.decode(caption[0], skip_special_tokens=True)


def get_content_description(content_title, content_body):
    """
    Generate a description for the content using the Gemini AI API
    """
    GOOGLE_APIKEY = config("GOOGLE_APIKEY")
    genai.configure(api_key=GOOGLE_APIKEY)
    model = genai.GenerativeModel("gemini-1.5-pro-latest")

    prompt = f"""
    You are an expert writer. 
    Use this Content Title and Content Body of the blog to generate a nice introduction (that will serve as the blog's content description) for the blog. 
    Let the description be nice, catchy and make the reader more interested in reading the content of the blog.
    Let the description also be as human as possible - as those it was written by a human writer not an AI.

    Content Title = {content_title}

    Blog Content = {content_body}

    Note: Let your response only be the content description. Do not include any other information.
    """

    try:
        response = model.generate_content(prompt)
        return response.candidates[0].content.parts[0].text.strip() if response.candidates else "No response from Gemini AI API"
    except google.api_core.exceptions.GoogleAPIError as api_error:
        return f"API Error from Gemini AI: {api_error}"
    except Exception as e:
        return f"Unexpected Error from 'get_content_description()': {e}"
