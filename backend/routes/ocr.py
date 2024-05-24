from flask import Blueprint, request, send_file
from flask_login import login_required
import pytesseract
from PIL import Image
#from fpdf import FPDF
import io

ocr = Blueprint('ocr', __name__)

@ocr.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    # Perform OCR
    image = Image.open(file.stream)
    text = pytesseract.image_to_string(image)

    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)

    # Save PDF to a bytes buffer
    pdf_buffer = io.BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)

    return send_file(pdf_buffer, as_attachment=True, download_name='output.pdf')
