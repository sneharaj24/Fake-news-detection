from flask import Flask, request, render_template, redirect, url_for
import os
import google.generativeai as genai
from news_detection import get_news_status

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'tmp')

# Ensure tmp folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

genai.configure(api_key='Enter you API KEY')  

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', news_text="", status=None)

@app.route('/predict', methods=['POST'])
def process_image():
    if 'input' not in request.files:
        return redirect(url_for('home'))

    file = request.files['input']
    if file.filename == '':
        return redirect(url_for('home'))

    ext = file.filename.split('.')[-1].lower()
    file_number = len(os.listdir(app.config['UPLOAD_FOLDER'])) + 1
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], f"{file_number}.{ext}")
    file.save(filepath)
    print(f"[INFO] Saved uploaded file: {filepath}")

    try:
       
        print("[INFO] Uploading file to Gemini...")python3
        sample_file = genai.upload_file(path=filepath)
        os.remove(filepath)
        print(f"[INFO] Upload success: {sample_file.name}")

        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-002")
        prompt = "Please extract and return only the news article text from this image."
        response = model.generate_content([prompt, sample_file])

        response_text = response.text.strip()
        if not response_text:
            raise ValueError("Empty OCR response")

        news = response_text.split(':', 1)[-1].strip() if ':' in response_text else response_text


        status = get_news_status(news)
        print(f'\n[OCR OUTPUT]: {news}\n[FAKE NEWS STATUS]: {"REAL" if status else "FAKE"}')

        return render_template('result.html', news_text=news, status=status)

    except Exception as e:
        print(f"[ERROR] {e}")
        return render_template('result.html', news_text="Error processing image.", status=None)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
