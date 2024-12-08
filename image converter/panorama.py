import cv2
import easygui

# Step 1: Allow the user to select multiple image files
file_paths = easygui.fileopenbox(title="Select 5 Images for Panorama", filetypes=["*.jpg", "*.png", "*.jpeg"], multiple=True)
if not file_paths or len(file_paths) < 2:
    print("Please select at least 2 images. Exiting...")
    exit()

# Step 2: Read the selected images
images = []
for file_path in file_paths:
    image = cv2.imread(file_path)
    if image is not None:
        images.append(image)
    else:
        print(f"Error loading image: {file_path}")
        exit()

# Step 3: Create a stitcher object
stitcher = cv2.Stitcher.create()

# Step 4: Stitch the images together
print("Stitching images, please wait...")
status, panorama = stitcher.stitch(images)

# Step 5: Handle stitching results
if status == cv2.Stitcher_OK:
    print("Panorama created successfully!")
    cv2.imshow("Panorama", panorama)
    
    # Save the result
    cv2.imwrite("panorama.jpg", panorama)
    print("Panorama saved as 'panorama.jpg'")
else:
    print(f"Error during stitching: {status}")

cv2.waitKey(0)
cv2.destroyAllWindows()
