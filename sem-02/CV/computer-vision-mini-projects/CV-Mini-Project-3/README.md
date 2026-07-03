# Detecting Harris Corners and Matching Images  
## Date: March 15, 2025
## Overview  
This project implements **Harris Corner Detection** and **keypoint matching** for two similar images. The goal is to identify significant corner points in both images using the Harris Corner Detection algorithm and then match corresponding keypoints between them.  

## Project Description  
This project consists of two main tasks:  

1. **Harris Corner Detection**:  
   - Convert the image to grayscale.  
   - Compute **Sobel derivatives** ($I_x$, $I_y$) to measure intensity changes.  
   - Construct the **second-moment matrix (M)** using ($I_x$, $I_y$).  
   - Compute the **corner response function (R)** using:  $$[R = \text{det}(M) - \alpha (\text{trace}(M))^2\]$$  
   - Identify strong corner points based on the computed response values.  

2. **Keypoint Creation and Matching**:  
   - Select keypoints from the detected Harris corners.  
   - Extract gradient-based keypoint descriptors.  
   - Match the **best 100** keypoints between two images.  

## Features Implemented  
1. **Harris Corner Detector**  
2. **Gradient-based Keypoint Extraction**  
3. **Keypoint Matching between Two Images**  
4. **Visualization of Keypoints and Matched Points**  

## Results  
- Successfully detected Harris corners in two images.  
- Extracted keypoints and matched the best 100 between the images.  
- Visualized Sobel derivatives, corner response function, detected keypoints, and matched keypoints.  

## Dependencies  
Ensure you have the following dependencies installed:  

```bash
pip install numpy matplotlib opencv-python
