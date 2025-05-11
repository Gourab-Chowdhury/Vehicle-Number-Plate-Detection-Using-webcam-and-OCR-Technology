# License Plate Detection and OCR

This is a Python-based application for detecting license plates in images or webcam feeds and extracting text from them using multiple OCR (Optical Character Recognition) libraries. It supports EasyOCR, PaddleOCR, Tesseract, and the Google Vision API.

---

## 🚀 Features

- **License Plate Detection**: Uses OpenCV to detect license plates in images or live webcam feeds.
- **Multi-OCR Support**: Extracts text from license plates using:
  - EasyOCR
  - PaddleOCR
  - PaddlePaddle
  - Tesseract OCR
  - Google Vision API
- **Image Preprocessing**: Includes resizing, grayscale conversion, noise reduction, and edge detection to enhance OCR performance.

---

## 📁 Project Structure

```
├── EasyOCR.py            # Uses EasyOCR for text extraction
├── PaddleOCR.py          # Uses PaddleOCR for text extraction
├── TesseractOCR.py       # Uses Tesseract OCR for text extraction
├── googleC.py            # Uses Google Vision API for text extraction
├── preprosseing.py       # Image preprocessing 
├── CarPictures/          # Directory for storing input 

images
│   ├── captured_car.jpg  # Captured image from webcam
│   ├── 001.jpg, 002.jpg  # Sample car images

```

---

## Requirements

- Python 3.7 or higher
- Required Python libraries:
  - OpenCV
  - Imutils
  - EasyOCR
  - PaddleOCR
  - Pytesseract
  - Google Cloud Vision API client

Install the dependencies using pip:

```bash
pip install opencv-python imutils easyocr paddleocr pytesseract google-cloud-vision
```

### Tesseract OCR

- Download and install from [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract).
- Update the path to the Tesseract executable in `TesseractOCR.py`:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  ```

### Google Cloud Vision API

- Create a Google Cloud project and enable the Vision API.
- Download your service account key (JSON).
- Set the environment variable in `googleC.py`:
  ```python
  os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your-service-account-file.json"
  ```

---

## 🎥 Webcam Access

Ensure your system has a functional webcam. You can also use saved images from the `CarPictures/` directory.

---

## ⚙️ Usage

1. **Preprocessing & Detection**  
   Run `preprosseing.py` to:
   - Capture an image from the webcam or process an existing image.
   - Detect the license plate.
   - Save it as `plate.png`.

2. **Run Individual OCR Engines**:
   - EasyOCR: `python EasyOCR.py`
   - PaddleOCR: `python PaddleOCR.py`
   - Tesseract OCR: `python TesseractOCR.py`
   - Google Vision API: `python googleC.py`

---

## 📤 Output

- Detected license plate image is saved as `plate.png`.
- Extracted text is printed to the terminal for each OCR engine.

---

## 📝 Example Output

```
Captured image: CarPictures/captured_car.jpg
Detected license plate saved as: plate.png

EasyOCR Result: MH12AB1234
PaddleOCR Result: MH12AB1234
Tesseract Result: MH12AB1234
Google Vision Result: MH12AB1234
```

---

## 🔧 Notes

- For best accuracy, use high-resolution and well-lit images.
- You can tweak preprocessing parameters (e.g., Canny edge thresholds) in `preprosseing.py` to improve detection results.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
