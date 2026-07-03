# Detection of Lines and Circles using Hough Transform Algorithm

## Date: February 24, 2025
## Overview
This project implements Hough Transform-based methods to detect **lines** and **circles** in images using edge detection and vote accumulation.

## Methods Implemented
- **`hough_lines_vote_acc`**: Detects lines using the Hough Transform by accumulating votes in Hough space.
- **`hough_circles_vote_acc`**: Detects circles by iterating over potential center points and radii.

## Methodology
- **Edge Detection**: Applied Gaussian blur and Canny edge detection to preprocess images.
- **Hough Transform**:
  - For **lines**, accumulated votes for different values of \( \rho \) and \( \theta \).
  - For **circles**, computed potential center points using a fixed radius.

## Results
- Successfully detected lines and circles in an image of a study table.
- Visualized Hough space with peak points highlighted.
