# Image Filtering and Hybrid Image Creation
## Date: February 10, 2025
## Overview

This project implements two key image processing functions: `my_imfilter` and `create_hybrid_image`. These functions perform image filtering and hybrid image generation by combining low-frequency and high-frequency components from different images.

## Features

- **Custom Image Filtering (`my_imfilter`)**: Applies a convolution-based filter to an image using a manually implemented convolution operation.
- **Hybrid Image Generation (`create_hybrid_image`)**: Combines the low-frequency content of one image with the high-frequency content of another to create a visually compelling hybrid image.
- **Support for Multiple Filters**:
  - Identity Filter
  - Small Blur Filter
  - Large 1D Gaussian Blur Filter
  - Oriented Sobel Filter (Edge Detection)
  - High-Pass Laplacian Filter

## Methodology

### `my_imfilter` Function

- **Objective**: Applies a convolution filter to an image manually.
- **Padding**: Zero-padding is applied to maintain output dimensions.
- **Implementation**:
  - Iterates over the image pixel by pixel.
  - Applies a convolution kernel to compute the filtered output.
  - Processes each RGB channel independently.

### `create_hybrid_image` Function

- **Objective**: Generates a hybrid image by combining frequency components from two images.
- **Steps**:
  - Apply a **Gaussian low-pass filter** to extract low-frequency content.
  - Extract **high-frequency content** by subtracting the filtered image from the original.
  - Combine both to generate the final hybrid image.
  - Ensure pixel values are clipped between [0,1] for proper visualization.

## Results

### Sample Filters Applied

| Filter Type | Description |
|------------|------------|
| **Identity Filter** | Preserves the original image. |
| **Small Blur Filter** | Averages neighboring pixels for a mild smoothing effect. |
| **Large Gaussian Blur Filter** | Stronger smoothing effect using a larger kernel. |
| **Sobel Filter** | Edge detection using a horizontal gradient filter. |
| **Laplacian Filter** | High-pass filter to detect edges and fine details. |

### Hybrid Image Generation

A Gaussian filter with a cutoff frequency of 7 was used to extract the low-frequency content, while high-frequency details were retained from another image. The combination results in a hybrid image where different details emerge depending on viewing distance.

## Code Structure

