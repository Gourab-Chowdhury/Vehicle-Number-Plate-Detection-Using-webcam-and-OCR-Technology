import cv2
import runpy
import easyocr

# Run the pre-processing script
runpy.run_path("preprosseing.py")

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])  # Specify 'en' for English
results = reader.readtext('plate.png', detail=0)  # Extracts text with detail=0 to only get plain text
# Combine detected text and clean up non-alphanumeric characters
plate_text = ''.join(''.join(results).split())  # Joins all words, then removes non-alphanumeric
plate_text = ''.join(char for char in plate_text if char.isalnum())
print("Detected Plate Text (EasyOCR):", plate_text)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()