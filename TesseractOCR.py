import cv2
import runpy
import pytesseract

# Run the pre-processing script
runpy.run_path("preprosseing.py")

# Tesseract OCR
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"   # Specify the path to Tesseract-OCR executable
text=pytesseract.image_to_string('plate.png',lang='eng')
# text = ''.join(e for e in text if e.isalnum())  #modify our text no spaces
print("Detected Plate Text (Tesseract):", text)
text = ''.join(e for e in text if e.isalnum())  #modify our text no spaces

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()