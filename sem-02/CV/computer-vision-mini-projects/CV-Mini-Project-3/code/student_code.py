import numpy as np
import cv2 
import matplotlib.pyplot as plt
# You must not use cv2.cornerHarris()
# You must not add any other library


### If you need additional helper methods, add those. 
### Write details description of those

"""
  Returns the harris corners,  image derivative in X direction,  and 
  image derivative in Y direction.
  Args
  - image: numpy nd-array of dim (m, n, c)
  - window_size: The shaps of the windows for harris corner is (window_size, wind)
  - alpha: used in calculating corner response function R
  - threshold: For accepting any point as a corner, the R value must be 
   greater then threshold * maximum R value.
  - nms_size = non maximum suppression window size is (nms_size, nms_size) 
    around the corner
  Returns 
  - corners: the list of detected corners
  - Ix: image derivative in X direction
  - Iy: image derivative in Y direction

"""
def harris_corners(image, window_size=5, alpha=0.04, threshold=1e-2, nms_size=10):

    ### YOUR CODE HERE
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    Ix = cv2.Sobel(image, cv2.CV_64F, 1,0,ksize=3)
    Iy = cv2.Sobel(image, cv2.CV_64F, 0,1,ksize=3)
    
    Ixx = Ix**2
    Iyy = Iy**2
    Ixy = Ix*Iy
    
    Ixx = cv2.GaussianBlur(Ixx, (window_size, window_size), 0) # noise add kore corner pai maane bhalo
    Iyy = cv2.GaussianBlur(Iyy, (window_size, window_size), 0)
    Ixy = cv2.GaussianBlur(Ixy, (window_size, window_size), 0)
    
    detM = Ixx*Iyy - (Ixy**2) # (\lambda1 * \lambda2)
    traceM = Ixx+Iyy # (\lambda1 + \lambda2)
    R = detM - alpha*(traceM**2) # dimension same as image
    
    fig, axes = plt.subplots(4, 3, figsize=(15, 15))
    axes[0,0].imshow(Ix, cmap="gray")
    axes[0,0].set_title("Ix")
    axes[0,1].imshow(Iy, cmap="gray")
    axes[0,1].set_title("Iy")
    axes[1,0].imshow(Ixx, cmap="gray")
    axes[1,0].set_title("Ixx")
    axes[1,1].imshow(Iyy, cmap="gray")
    axes[1,1].set_title("Iyy")
    axes[1,2].imshow(Ixy, cmap="gray")
    axes[1,2].set_title("Ixy")
    axes[2,0].imshow(detM, cmap="gray")
    axes[2,0].set_title("detM")
    axes[2,1].imshow(traceM, cmap="gray")
    axes[2,1].set_title("traceM")
    axes[2,2].imshow(R, cmap="gray")
    axes[2,2].set_title("R")
    
    
    
    corners = np.zeros_like(R) # ReLU-like matrix (non-zero if above threshold=R)
    K = nms_size//2 # nms = non-maximum supression
    
    for i in range(K, R.shape[0]-K):
        for j in range(K, R.shape[1]-K):
            window = R[(i-K):(i+K+1), (j-K):(j+K+1)]
            if R[i,j] == np.max(window):
                corners[i,j] = R[i,j]
    
    axes[3,0].imshow(corners, cmap="gray")
    axes[3,0].set_title("before threshold")
    
    print("number of corners before thresholding =", np.unique(corners).size)
    
    
    maxi_R = np.max(R)
    corners[R<threshold*maxi_R] = 0

    print("number of corners after thresholding =", np.unique(corners).size)

    axes[3,1].imshow(corners, cmap="gray")
    axes[3,1].set_title("after threshold")
    
    return corners, Ix, Iy


"""
  Creates key points form harris corners and returns the list of keypoints. 
  You must use cv2.KeyPoint() method. 
  Args
  - corners:  list of Normalized corners.  
  - Ix: image derivative in X direction
  - Iy: image derivative in Y direction
  - threshold: only select corners whose R value is greater than threshold
  
  Returns 
  - keypoints: list of cv2.KeyPoint
  
  Notes:
  You must use cv2.KeyPoint() method. You should also pass 
  angle of gradient at the corner. You can calculate this from Ix, and Iy 

"""
def get_keypoints(corners, Ix, Iy, threshold):
    
    ### YOUR CODE HERE
    
    m = corners.shape[0]
    n = corners.shape[1]
    
    keypoints=[]
    
    for i in range(m):
        for j in range(n):
            if corners[i,j]>threshold:
                angle = np.arctan2(Iy[i,j],Ix[i,j])*180/np.pi  # Since angle = tan_inv(y/x)
                print("keypoint = (", i, j, ")", "corners[i,j] =", corners[i,j], "threshold =", threshold)
                keypoint = cv2.KeyPoint(x=i,y=j,size=100,angle=angle)
                keypoints.append(keypoint)
    
    print("number of keypoints =", len(keypoints))
    
    return keypoints
