import cv2
import numpy as np

# Define HSV color ranges for green, red, and yellow
green_lower = np.array([40, 50, 50])
green_upper = np.array([90, 255, 255])

red_lower = np.array([0, 70, 50])
red_upper = np.array([10, 255, 255])
red_lower_2 = np.array([170, 70, 50])
red_upper_2 = np.array([180, 255, 255])

yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([30, 255, 255])

# Function to classify the light based on color range using OpenCV inRange
def classify_traffic_light(image_path):
    # Load image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Green light detection
    green_mask = cv2.inRange(hsv_image, green_lower, green_upper)
    if np.any(green_mask):
        return "Green Light"
    
    # Red light detection (both low and high hue range)
    red_mask1 = cv2.inRange(hsv_image, red_lower, red_upper)
    red_mask2 = cv2.inRange(hsv_image, red_lower_2, red_upper_2)
    if np.any(red_mask1) or np.any(red_mask2):
        return "Red Light"
    
    # Yellow light detection
    yellow_mask = cv2.inRange(hsv_image, yellow_lower, yellow_upper)
    if np.any(yellow_mask):
        return "Yellow Light"
    
    return "Unknown Light"

# Example of using the function with one of the uploaded images
image_path = 'light_sign/red.jpg'  # You can change this path to red_image_path or yellow_image_path
result = classify_traffic_light(image_path)
print(result)
