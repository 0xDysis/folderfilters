import cv2
import numpy as np
import os
import shutil

# Define the color ranges
color_ranges = {
    'blue': ([100, 0, 0], [255, 100, 100]),
    'green': ([0, 100, 0], [100, 255, 100]),
    'red': ([0, 0, 100], [100, 100, 255]),
    'black_and_white': ([0, 0, 0], [255, 255, 255])
}

# Define the directories
directories = ['Landscape', 'Portrait', 'Square']

# Loop over the directories
for directory in directories:
    # Loop over the files in the directory
    for filename in os.listdir(directory):
        # Read the image
        image = cv2.imread(os.path.join(directory, filename))

        # Convert the image to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Calculate the mean color of the image
        mean_color = np.mean(image, axis=(0, 1))

        # Loop over the color ranges
        for color, (lower, upper) in color_ranges.items():
            # Check if the mean color is in the color range
            if all(lower <= mean_color) and all(mean_color <= upper):
                # Create the subdirectory if it doesn't exist
                if not os.path.exists(os.path.join(directory, color)):
                    os.makedirs(os.path.join(directory, color))

                # Move the file to the subdirectory
                shutil.move(os.path.join(directory, filename), os.path.join(directory, color, filename))

                # Stop checking colors
                break