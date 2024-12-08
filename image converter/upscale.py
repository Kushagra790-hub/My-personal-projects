import cv2
import easygui

# Step 1: Ask the user to select an image file
file_path = easygui.fileopenbox(title="Select an Image File", filetypes=["*.jpg", "*.png", "*.jpeg", "*.bmp"])
if file_path is None:
    print("No file selected. Exiting...")
    exit()

# Step 2: Load the image
image = cv2.imread(file_path)
if image is None:
    print("Error: Unable to load image. Exiting...")
    exit()

# Step 3: Ask the user for scaling factors
scale_x = float(input("Enter the scaling factor for width (e.g., 2.0 for doubling width): "))
scale_y = float(input("Enter the scaling factor for height (e.g., 2.0 for doubling height): "))

# Step 4: Upscale using Bilinear Interpolation
bilinear_upscaled = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)

# Step 5: Upscale using Bicubic Interpolation
bicubic_upscaled = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_CUBIC)

# Step 6: Display results
cv2.imshow("Original Image", image)
cv2.imshow("Bilinear Upscaled Image", bilinear_upscaled)
cv2.imshow("Bicubic Upscaled Image", bicubic_upscaled)

# Save results
cv2.imwrite("bilinear_upscaled.jpg", bilinear_upscaled)
cv2.imwrite("bicubic_upscaled.jpg", bicubic_upscaled)

print("\nUpscaled images have been saved as 'bilinear_upscaled.jpg' and 'bicubic_upscaled.jpg'.")

cv2.waitKey(0)
cv2.destroyAllWindows()
