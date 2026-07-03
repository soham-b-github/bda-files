import numpy as np
import matplotlib.pyplot as plt
#### DO NOT IMPORT cv2 

def my_imfilter(image, filter):
		
		"""
		Apply a filter to an image. Return the filtered image.

		Args
		 - image: numpy nd-array of dim (m, n, c)
		 - filter: numpy nd-array of dim (k, k)
		 Returns
		 - filtered_image: numpy nd-array of dim (m, n, c)

		HINTS:
		 - You may not use any libraries that do the work for you. Using numpy to work
		  with matrices is fine and encouraged. Using opencv or similar to do the
		  filtering for you is not allowed.
		 - I encourage you to try implementing this naively first, just be aware that
		  it may take an absurdly long time to run. You will need to get a function
		  that takes a reasonable amount of time to run so that I can verify
		  your code works.
		 - Remember these are RGB images, accounting for the final image dimension.
		 """

		assert filter.shape[0] % 2 == 1
		assert filter.shape[1] % 2 == 1

		############################
		### TODO: YOUR CODE HERE ###
			
		m,n,c = image.shape
		K = filter.shape[0]  # Assuming square filter
		pad_size = K//2
		
		# Padding the image with zeros to handle border cases
		padded_image = np.pad(image, ((pad_size, pad_size), (pad_size, pad_size), (0, 0)), mode='constant')
		plt.imshow(padded_image)
		
		# Initialize output image
		filtered_image = np.zeros_like(image)
		
		# Convolution
		for i in range(m):
			for j in range(n):
				for ch in range(c): # ch stands for channel, iterating for each color channel
					region = padded_image[i:i+K, j:j+K, ch]
					filtered_image[i, j, ch] = np.sum(region * filter)



		### END OF STUDENT CODE ####
		############################

		return filtered_image

def create_hybrid_image(image1, image2, filter):
		
		"""
		Takes two images and creates a hybrid image. Returns the low
		frequency content of image1, the high frequency content of
		image 2, and the hybrid image.

		Args
		- image1: numpy nd-array of dim (m, n, c)
		- image2: numpy nd-array of dim (m, n, c)
		Returns
		- low_frequencies: numpy nd-array of dim (m, n, c)
		- high_frequencies: numpy nd-array of dim (m, n, c)
		- hybrid_image: numpy nd-array of dim (m, n, c)

		HINTS:
		- You will use your my_imfilter function in this function.
		- You can get just the high frequency content of an image by removing its low
		frequency content. Think about how to do this in mathematical terms.
		- Don't forget to make sure the pixel values are >= 0 and <= 1. This is known
		as 'clipping'.
		- If you want to use images with different dimensions, you should resize them
		in the notebook code.
		"""

		assert image1.shape[0] == image2.shape[0]
		assert image1.shape[1] == image2.shape[1]
		assert image1.shape[2] == image2.shape[2]

		############################
		### TODO: YOUR CODE HERE ###

		# Apply low-pass filter to image1
		low_frequencies = my_imfilter(image1, filter)
		
		# Get high-frequency content from image2
		high_frequencies = image2 - my_imfilter(image2, filter)
		
		# Combine low and high frequencies
		hybrid_image = low_frequencies + high_frequencies
		
		# Clip values to be in valid range (0 to 1)
		hybrid_image = np.clip(hybrid_image, 0, 1)

		### END OF STUDENT CODE ####
		############################

		return low_frequencies, high_frequencies, hybrid_image
