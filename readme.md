```markdown
# QR Code Generator using Python

## Project Overview
This project implements a simple QR Code Generator using Python and the `qrcode` library. The application allows the user to input a URL, validates the input, and generates a QR code image. The generated QR code can be saved locally and opened for viewing. This aligns with the assignment requirement to create a QR code generator in Python.

QR codes are widely used for encoding URLs and other data in a format that can be easily scanned by smartphones and other devices. This project demonstrates how Python can be used to automate QR code generation with just a few lines of code.

## Features
- Accepts URL input via command-line or interactive prompt.
- Validates the URL to ensure it is well-formed (http or https).
- Generates a QR code image and saves it in the `output/` folder.
- Opens the QR code image automatically for easy preview.
- Supports customization of:
  - Error correction levels: L, M, Q, H
  - Box size (pixel size of each QR module)
  - Border (quiet zone around the QR code)

## Technical Requirements
- Python 3.x
- Libraries:  
  - `qrcode`  
  - `Pillow` (installed automatically with `qrcode[pil]`)

## Setup Instructions

1. Clone the repository
   ```bash
   git clone <your_repo_url>
   cd qr-generator
   ```

2. Create and activate virtual environment
   - macOS/Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - Windows (PowerShell):
     ```bash
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Interactive mode (prompts for URL):
```bash
python3 main.py
```

Non-interactive mode (pass URL and options):
```bash
python3 main.py --url https://www.example.com --ec M --box-size 10 --border 4
```

Arguments:
- `--url` : URL to encode
- `--ec` : Error correction level (L, M, Q, H)
- `--box-size` : Size of each module in pixels (default: 10)
- `--border` : Border width in modules (default: 4)
- `-o` : Output file path (default: `output/qr_<timestamp>.png`)

## Project Structure
```
qr-generator/
│── main.py                # Main Python script
│── requirements.txt       # Manifest of required libraries
│── README.md              # Project documentation
│── output/                # Folder where QR images are saved
│── assets/                # Screenshots for submission
```

## Example Output

Running:
```bash
python3 main.py --url https://ucumberlands.edu
```

Produces:
- Output file: `output/qr_20250906_132512.png`
- Preview window showing the QR code

Screenshot Example  
(Screenshot of the preview window should be saved as `assets/screenshot.png`)

## Testing and Validation
- Tested with multiple URLs, including:
  - Short URLs (`https://google.com`)
  - Long URLs (`https://www.example.com/some/long/path?with=query&params=value`)
- Verified that QR codes scan correctly with mobile devices.
- Handled invalid inputs (e.g., missing `http://` or blank string).

## Deliverables
As per assignment instructions:
1. Python source code: `main.py`
2. Manifest file: `requirements.txt`
3. Screenshot: `assets/screenshot.png`
4. Repository link: GitHub repo containing all files

## Comments
- The implementation follows Python coding best practices with comments explaining major functions.
- Error correction level defaults to M for a balance of capacity and robustness.
- The project is extensible: it could easily be expanded with a GUI (Tkinter) or batch QR generation.

## Author
- Name: Murali Krishna Chintha  
- Course: MSCS – Advanced Big Data and Data Mining (MSCS-634-M40)  
- Institution: University of the Cumberlands
```

