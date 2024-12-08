import cv2
import numpy as np
import pandas as pd
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

# Step 3: Ask if the user wants grayscale or color
mode = input("Do you want to save the image as grayscale or color? Enter 'gray' or 'color': ").strip().lower()

if mode == 'gray':
    # Convert to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Save as a CSV file
    csv_data = pd.DataFrame(image)  # Each row corresponds to a row of pixels
    output_file = "image_grayscale.csv"
else:
    # Flatten color channels and save as a CSV file
    image_reshaped = image.reshape(-1, 3)  # Reshape into (N, 3) where N = width*height
    csv_data = pd.DataFrame(image_reshaped, columns=["Blue", "Green", "Red"])
    output_file = "image_color.csv"

# Step 4: Save to CSV
csv_data.to_csv(output_file, index=False)
print(f"Image data saved as '{output_file}'.")

