import cv2
import imutils  # for resizing images

# Capture and save an image from the webcam
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    cv2.imshow('Webcam Feed', frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):  # Press 'c' to capture and save the image
        break
    cv2.imwrite('CarPictures/captured_car.jpg', frame)
video_capture.release()
cv2.destroyAllWindows()


# Load and preprocess the saved image

# image = cv2.imread('CarPictures/005.jpg')
image = cv2.imread('CarPictures/captured_car.jpg')
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







































'''
Algorithm: License Plate Detection and Cropping
https://chatgpt.com/share/6731f7c5-a064-8008-af60-de0cf370451b
Step 1: Load and Preprocess the Image
Load the target image using cv2.imread.
Resize the image to a standard width (500 pixels) using imutils.resize for consistency in processing.
Display the original resized image.

Step 2: Convert Image to Grayscale
Convert the resized image to grayscale using cv2.cvtColor.
Display the grayscale image, which helps reduce complexity and prepares the image for contour detection.

Step 3: Apply Smoothing to Reduce Noise
Apply a bilateral filter (cv2.bilateralFilter) on the grayscale image to smooth it while preserving edges.
This helps to reduce noise, which is useful for edge detection.
Display the smoothed grayscale image.

Step 4: Detect Edges
Use the Canny edge detection algorithm (cv2.Canny) to identify the edges in the smoothed image.
Display the edges image, highlighting the contours of objects in the image.

Step 5: Find and Draw Contours
Find all contours in the edge-detected image using cv2.findContours.
Copy the original image and draw all detected contours on it with cv2.drawContours.
Display this image to visualize all detected contours.

Step 6: Filter and Sort Contours by Size
Sort the detected contours by area, selecting the largest 30 contours, as larger contours are more likely to contain the license plate.
Copy the original image and draw the top 30 largest contours on it.
Display the image to visualize the largest contours.

Step 7: Identify License Plate Contour
Iterate through the top 30 contours to find one resembling a license plate shape:
Calculate the perimeter of each contour using cv2.arcLength.
Approximate each contour to a polygon with reduced points using cv2.approxPolyDP.
Identify the contour that has exactly 4 corners, as a rectangle shape (4 corners) is likely to match a license plate.
If a 4-corner contour is found, consider it the license plate contour:
Use cv2.boundingRect to get coordinates (x, y) and dimensions (w, h) of this contour.
Crop this region from the original image to isolate the number plate.
Save the cropped image as plate.png.

Step 8: Draw and Display the Detected License Plate Contour
If a license plate contour was identified:
Draw this contour on the original image using cv2.drawContours.
Display the modified image showing the detected license plate.
Display the cropped license plate image stored in plate.png.
'''