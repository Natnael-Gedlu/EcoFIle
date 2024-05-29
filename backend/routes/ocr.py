from flask import Blueprint, request, jsonify, send_file, current_app
from flask_login import login_required
from PIL import Image, ImageDraw
import pytesseract
import io
import os
from werkzeug.utils import secure_filename

ocr = Blueprint('ocr', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@ocr.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Open the image file
        image = Image.open(file_path)

        # Perform OCR on the image
        ocr_text = pytesseract.image_to_string(image)

        # For demonstration, we will just draw the text back on the image
        image_editable = ImageDraw.Draw(image)
        image_editable.text((15, 15), ocr_text, (0, 0, 0))

        # Save the edited image to a bytes buffer
        buf = io.BytesIO()
        image.save(buf, format='PNG')
        buf.seek(0)

        # Return the edited image
        return send_file(buf, mimetype='image/png', as_attachment=True, download_name='output.png')

    return jsonify({'message': 'File not allowed'}), 400
