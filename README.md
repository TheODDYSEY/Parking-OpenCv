Parking Space Monitoring System using OpenCV
This project is a Parking Space Monitoring System that uses OpenCV (Open Source Computer Vision Library) to analyze a video feed from a car park and determine the availability of parking spaces. The system processes the video frames, applies image processing techniques, and then identifies the number of free parking spaces in real-time.


Requirements

Clone this project 

https://github.com/TheODDYSEY/Parking-OpenCv.git


To run this project, you will need the following software and libraries:

Python 3.x
OpenCV (cv2)
NumPy (numpy)
Pickle (pickle)
CVZone (cvzone)

You can install the required libraries using pip:

pip install opencv-python numpy pickle-mixin cvzone

Usage
Download the project files, including the car park video (carPark.mp4) and the serialized position data (CarParkPos).
Make sure you have the required libraries installed (see Requirements).
Execute the Python script (parking_space_monitoring.py).
The script will load the video and process each frame to determine the number of free parking spaces.
The output will display the video with rectangles drawn around parking spaces, indicating their status (free or occupied).
How it works
The system uses pre-defined parking space positions (stored in CarParkPos using Pickle) to extract individual parking spaces from each video frame.

The system converts the color frame into a grayscale image and applies Gaussian Blur to reduce noise and enhance the image.

It then converts the grayscale image into a binary image (white lines on a black background) using adaptive thresholding.

To remove remaining noise pixels, a median blur operation is performed on the binary image.

A dilation operation is applied to the image to make the parking spaces more prominent and to fill any gaps.

For each parking space, the number of non-zero (white) pixels is counted in the binary image. Fewer non-zero pixels indicate a free parking space, and more pixels indicate an occupied parking space.

The number of free parking spaces is displayed on the output video, along with rectangles drawn around each parking space, representing their status (free or occupied).

References
OpenCV: https://opencv.org/
NumPy: https://numpy.org/
Pickle: https://docs.python.org/3/library/pickle.html
CVZone: https://github.com/cvzone/cvzone
Note: The CarParkPos file should contain the serialized list of parking space positions (x, y coordinates) that are relevant to the provided car park video. This file is crucial for the correct functioning of the system, and its format should be compatible with the pickle.load() function. Make sure to provide the correct file with the accurate parking space positions to get accurate results.

Additionally, this project assumes the video file is present in the specified path (./media/carPark.mp4). If the video is not available or the path is incorrect, the system may not work as expected. Please ensure that the video is accessible before running the script.
