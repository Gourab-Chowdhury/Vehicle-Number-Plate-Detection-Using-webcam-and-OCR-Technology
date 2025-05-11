import cv2
import runpy
from paddleocr import PaddleOCR

# Run the pre-processing script
runpy.run_path("preprosseing.py")



# Initialize PaddleOCR model
ocr = PaddleOCR(lang='en')  # Specify language

# Extract text from image
result = ocr.ocr('plate.png', cls=True)  # Classifies each line

# Flatten result to get just text
plate_text = ''.join([line[1][0] for line in result[0]])  # Extracts recognized text
plate_text = ''.join(char for char in plate_text if char.isalnum())
print("Detected Plate Text (PaddleOCR):", plate_text)



if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()