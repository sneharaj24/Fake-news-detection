# gemini_test.py

from PIL import Image
import io

def image_text_input(image_file, news_text):
    try:
        # Safely open image from uploaded file stream
        image = Image.open(io.BytesIO(image_file.read()))

        # Reset stream position if reused
        image_file.seek(0)

        # Dummy result or your actual processing logic
        result = f"Processed image and news: '{news_text[:50]}...'"
        return result

    except Exception as e:
        print(f"Error in image_text_input: {e}")
        return "error in image processing"
