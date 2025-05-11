import cv2
import imutils  # for resizing images
# import pytesseract
# from pymongo import MongoClient

# Set path for Tesseract OCR executable
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017/")  # Adjust as needed for remote connections
# db = client["vehicle_database"]
# collection = db["registered_vehicles"]

# Capture and save an image from the webcam
# video_capture = cv2.VideoCapture(0)
# while True:
#     ret, frame = video_capture.read()
#     cv2.imshow('Webcam Feed', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to capture and save the image
#         break
#     cv2.imwrite('CarPictures/captured_car.jpg', frame)
# video_capture.release()
# cv2.destroyAllWindows()

# Load and preprocess the saved image
image = cv2.imread('CarPictures/006.jpg')
image = imutils.resize(image, width=500)
cv2.imshow("Original Image", image)

# Convert the image to grayscale to reduce complexity
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_image)

# Smooth the grayscale image to reduce noise
smoothed_gray = cv2.bilateralFilter(gray_image, 11, 17, 17)
cv2.imshow("Smoothed Image", smoothed_gray)

# Detect edges to identify potential areas of interest
edges = cv2.Canny(smoothed_gray, 170, 200)
cv2.imshow("Edges", edges)

# Find contours to detect shapes in the image
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Draw all detected contours for visualization
contoured_image = image.copy()
cv2.drawContours(contoured_image, contours, -1, (0, 255, 0), 3)
cv2.imshow("All Contours", contoured_image)

# Sort contours by area to focus on the largest ones (potential number plates)
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
plate_contour = None

# Draw the top 30 contours for verification
top_contours_image = image.copy()
cv2.drawContours(top_contours_image, sorted_contours, -1, (0, 255, 0), 3)
cv2.imshow("Top 30 Contours", top_contours_image)

# Identify the contour that most likely represents the number plate
for contour in sorted_contours:
    perimeter = cv2.arcLength(contour, True)
    approx_corners = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    
    if len(approx_corners) == 4:  # A rectangle (4 corners) is likely a number plate
        plate_contour = approx_corners
        x, y, w, h = cv2.boundingRect(contour)
        cropped_plate = image[y:y+h, x:x+w]
        cv2.imwrite('plate.png', cropped_plate)  # Save the cropped number plate image
        break

# Draw the identified number plate contour on the original image
if plate_contour is not None:
    cv2.drawContours(image, [plate_contour], -1, (0, 255, 0), 3)
    cv2.imshow("Detected Plate", image)

# Show the cropped image of the number plate
cv2.imshow("Cropped Plate", cv2.imread('plate.png'))


from google.cloud import vision
import os

# Set up Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your-service-account-file.json"

# Initialize Vision API client
client = vision.ImageAnnotatorClient()

# Load image
with open('plate.png', 'rb') as image_file:
    content = image_file.read()
image = vision.Image(content=content)

# Perform OCR
response = client.text_detection(image=image)
texts = response.text_annotations

# Get the first (most prominent) result
plate_text = texts[0].description if texts else ""
plate_text = ''.join(char for char in plate_text if char.isalnum())
print("Detected Plate Text (Google Vision):", plate_text)



cv2.waitKey(0)
cv2.destroyAllWindows()