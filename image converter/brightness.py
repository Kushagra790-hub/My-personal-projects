import cv2
import numpy as np
import easygui

# Function to adjust brightness
def adjust_brightness(image, value):
    """
    Adjust the brightness of an image by adding a constant value.

    :param image: Input image (numpy array).
    :param value: Value to add to pixel intensity. Positive to increase brightness, negative to decrease.
    :return: Brightness-adjusted image.
    """
    brightness_adjusted = cv2.convertScaleAbs(image, alpha=1, beta=value)
    return brightness_adjusted

# Step 1: Ask the user to select an image file
file_path = easygui.fileopenbox(title="Select an Image File", filetypes=["*.jpg", "*.png", "*.jpeg", "*.bmp"])
if file_path is None:
    print("No file selected. Exiting...")
    exit()

# Step 2: Load the selected image
image = cv2.imread(file_path)
if image is None:
    print("Error: Unable to load image. Exiting...")
    exit()

# Step 3: Ask the user for a brightness adjustment value
print("\nEnter a brightness adjustment value:")
print("- Positive value to increase brightness.")
print("- Negative value to decrease brightness.")
value = int(input("Enter the adjustment value (e.g., 50 or -50): "))

# Step 4: Adjust the brightness of the image
brightened_image = adjust_brightness(image, value)

# Step 5: Display the original and adjusted images
cv2.imshow("Original Image", image)
cv2.imshow("Brightness Adjusted Image", brightened_image)

# Step 6: Save the adjusted image
output_path = "brightness_adjusted.jpg"
cv2.imwrite(output_path, brightened_image)
print(f"\nBrightness adjusted image saved as '{output_path}'.")

cv2.waitKey(0)
cv2.destroyAllWindows()
