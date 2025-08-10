from flask import Flask, request
import time,logging
from PIL import Image
import pytesseract
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
# pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

@app.route('/')
def home():
    return "home"

@app.route('/about')
def about():
    return "<p>about page</p>"

@app.route('/uploadimg',methods=['POST'])
def upload_image():

    count=0
    try:
        image_data = request.data
        filename = f'image_{int(count)}.jpg'
        count+=1
        # print(image_data)

        with open(filename, 'wb') as f:
            f.write(image_data)
            # return f'Image saved as {filename}'
        
        print(f"Image saved as {filename}")
        print(f"Received {len(image_data)} bytes")
        return 'recive',200
    
        # img=Image.open(filename)
        # if(img==None):
        #     return "❌ Error: Image not found",200
        # else:
        #     pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'  # Update this path if necessary
        #     text = pytesseract.image_to_string(img)
        #     print("Extracted Text:", text)

            # print(f"Image saved as {filename}")
            # print(f"Received {len(image_data)} bytes")
            # return text,200
            
    except Exception as e:
        return f"❌ Error: {str(e)}", 500


@app.route('/uploaddata', methods=['POST'])
def handle_raw_data():

    count=0
    try:
        txt_data = request.data
        filename = f'text_{int(count)}.txt'
        count+=1
        # print(image_data)

        with open(filename, 'wb') as f:
            f.write(txt_data)
            # return f'Image saved as {filename}'

        print(f"Image saved as {filename}")
        print(f"Received {len(txt_data)} bytes")
        return "recive",200

    except Exception as e:
        return f"❌ Error: {str(e)}", 500



if __name__ == '__main__':
    app.run(debug=True, port=3001)
# -----------------------------------------



