import random
import requests
from decouple import config
import google.api_core.exceptions
import google.generativeai as genai
from google.generativeai import types
from cloudinary.uploader import upload

GOOGLE_APIKEY = config("GOOGLE_APIKEY")



def hash_generate(num_of_chars):
    """
    Generate a random string of numbers
    """
    return ''.join(random.choice('23456789') for _ in range(num_of_chars))


def upload_image_online(image_file):
    """
    Upload the image to Cloudinary
    """
    upload_result = upload(image_file)
    return upload_result['secure_url']


def generate_image_caption(local_image_url=None, online_image_url=None):
    """
    Generate an image caption for the image using Gemini AI via the API
    """
    try:
        genai.configure(api_key=GOOGLE_APIKEY)

        if local_image_url:
            # Handle ImageFieldFile objects
            if hasattr(local_image_url, 'path'):
                with open(local_image_url.path, 'rb') as f:
                    image_bytes = f.read()
            else:
                # If it's not a file path, assume it's a file-like object
                image_bytes = local_image_url.read()

            image = types.Part.from_bytes(data=image_bytes, mime_type='image/png')
            prompt = "Caption this image."
        elif online_image_url:
            image_bytes = requests.get(online_image_url).content
            image = types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg')
            prompt = "What is this image?"
        elif local_image_url and online_image_url:
            return "Both local and online image URLs provided. Please provide only one."
        else:
            return "No image path or URL provided."

        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(contents=[prompt, image])

        return response.candidates[0].content.parts[0].text.strip() if response.candidates else "No response from Gemini AI API"
    except requests.RequestException as req_error:
        return f"Error fetching online image: {req_error}"
    except google.api_core.exceptions.GoogleAPIError as api_error:
        return f"API Error from Gemini AI: {api_error}"
    except FileNotFoundError:
        return "Local image file not found."
    except Exception as e:
        return f"Unexpected Error in 'generate_image_caption()': {e}"
    

def get_content_description(content_title, content_body):
    """
    Generate a description for the content using the Gemini AI via the API
    """
    genai.configure(api_key=GOOGLE_APIKEY)
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
    You are an expert blog article writer. 
    Use this Content Title and Content Body of the blog to generate a nice introduction (that will serve as the blog article's content description) for the blog article. 
    Let the description be nice, catchy and make the reader more interested in reading the content of the blog.
    Let the description also be as human as possible - as though it was written by a human writer not an AI.

    Content Title = {content_title}

    Blog Content = {content_body}

    Note: Let your response only be the Content Description. Do not include any other information.
    """

    try:
        response = model.generate_content(prompt)
        return response.candidates[0].content.parts[0].text.strip() if response.candidates else "No response from Gemini AI API"
    except google.api_core.exceptions.GoogleAPIError as api_error:
        return f"API Error from Gemini AI: {api_error}"
    except Exception as e:
        return f"Unexpected Error from 'get_content_description()': {e}"
