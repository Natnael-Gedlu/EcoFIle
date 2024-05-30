#!/usr/bin/python3
"""
Defines routes for Optical Character Recognition (OCR) processing.
"""
from flask import Blueprint, request, jsonify, send_file
from flask_login import login_required
from PIL import Image
import pytesseract
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

ocr = Blueprint('ocr', __name__)


@ocr.route('/upload', methods=['POST'])
@login_required
def upload_file():
    """
        Handles file upload for OCR processing.

        Returns:
            JSON response with a message and status code, or
            the processed image file with OCR text.
        """
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file:
        # Open the image file
        image = Image.open(file.stream)

        # Perform OCR on the image
        ocr_text = pytesseract.image_to_string(image)

        # Create a PDF with the extracted text
        pdf_buffer = io.BytesIO()
        c = canvas.Canvas(pdf_buffer, pagesize=letter)
        width, height = letter

        # Set up the canvas for writing text
        c.setFont("Helvetica", 10)

        # Split the OCR text into lines and write them to the PDF
        y = height - 40  # Start a bit lower than the top edge
        for line in ocr_text.split('\n'):
            c.drawString(40, y, line)
            y -= 15  # Move down for the next line

            if y < 40:  # Check if we need a new page
                c.showPage()
                c.setFont("Helvetica", 10)
                y = height - 40

        c.save()
        pdf_buffer.seek(0)

        # Return the PDF file
        return send_file(pdf_buffer, mimetype='application/pdf', as_attachment=True, download_name='output.pdf')

    return jsonify({'message': 'No valid file found'}), 400
