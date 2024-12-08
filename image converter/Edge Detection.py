import cv2
import easygui

# File selection dialog
file_path = easygui.fileopenbox(title="Select an Image File", filetypes=["*.jpg", "*.png", "*.jpeg", "*.bmp"])

# Check if a file was selected
if file_path is None:
    print("No file selected. Exiting...")
    exit()

# Load the image in color
image = cv2.imread(file_path, cv2.IMREAD_COLOR)

# Compute gradients on each channel separately
gradients_sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
gradients_sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1)

# Combine Sobel x and y for visualization
gradients_sobelxy = cv2.addWeighted(gradients_sobelx, 0.5, gradients_sobely, 0.5, 0)

# Apply Laplacian (on each channel)
gradients_laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Convert to grayscale for Canny
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny_output = cv2.Canny(gray_image, 80, 150)

# Display results
cv2.imshow('Original Image', image)
cv2.imshow('Sobel x', cv2.convertScaleAbs(gradients_sobelx))
cv2.imshow('Sobel y', cv2.convertScaleAbs(gradients_sobely))
cv2.imshow('Sobel x+y', cv2.convertScaleAbs(gradients_sobelxy))
cv2.imshow('Laplacian', cv2.convertScaleAbs(gradients_laplacian))
cv2.imshow('Canny', canny_output)

cv2.waitKey(0)
cv2.destroyAllWindows()