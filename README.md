# EcoFile

**Digitize Your Documents with Ease**

EcoFile is a web application that allows users to upload scanned documents and convert them to PDF using Optical Character Recognition (OCR). The application also supports user registration and login to manage document processing securely.

## Features

- User Registration and Login
- OCR to extract text from scanned images
- Convert scanned images to PDF
- Secure user authentication
- Easy-to-use web interface

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Virtualenv
- Flask
- Node.js and npm (if using any frontend build tools)

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Natnael-Gedlu/EcoFile.git
    cd EcoFile
    ```

2. **Set Up the Backend**:

    - Create a virtual environment and activate it:
        ```bash
        python -m venv venv
        source venv/bin/activate  # On Windows: venv\Scripts\activate
        ```

    - Install the required Python packages:
        ```bash
        pip install -r requirements.txt
        ```

    - Initialize the database:
        ```bash
        flask db init
        flask db migrate -m "Initial migration"
        flask db upgrade
        ```

    - Run the Flask application:
        ```bash
        python backend/app.py
        ```

3. **Set Up the Frontend**:

    - Navigate to the `frontend` directory:
        ```bash
        cd frontend
        ```

    - Open `index.html` in your web browser.

### Project Structure

```bash
EcoFile/
├── backend/
│ ├── app.py
│ ├── config.py
│ ├── init.py
│ ├── models.py
│ ├── routes/
│ │ ├── init.py
│ │ ├── auth.py
│ │ ├── ocr.py
│ ├── static/
│ │ └── uploads/
│ └── templates/
│ └── index.html
├── frontend/
│ ├── index.html
│ ├── app.js
│ ├── style.css
├── migrations/
├── venv/
├── requirements.txt
├── .gitignore
└── README.md
```

### Usage

1. **Register a New User**:
    - Open the application in your browser.
    - Go to the registration form and create a new account.

2. **Login**:
    - Log in with your registered credentials.

3. **Upload and Convert Documents**:
    - After logging in, use the upload form to select a scanned document.
    - Click "Convert to PDF" to start the OCR and conversion process.
    - Download the generated PDF.

### Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact

For any questions or feedback, please reach out at [nategd800@gmail.com].

---

Thank you for using EcoFile!
