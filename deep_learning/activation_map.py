# Import numpy to perform array operations
import numpy as np

# Given input image matrix (assuming it's 8x8 based on the description)
image_matrix = np.array([
    [1, 1, 2, 2, 2, 0, 0],
    [2, 0, 1, 1, 2, 1, 2],
    [0, 1, 0, 0, 1, 1, 2],
    [0, 2, 1, 2, 0, 2, 2],
    [1, 2, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 2, 1],
    [0, 0, 0, 0, 0, 2, 1],
    [2, 0, 0, 0, 2, 1, 1]
])

# Given convolutional filter (kernel)
conv_filter = np.array([
    [0, 1, 1],
    [0, 1, 0],
    [0, -1, -1]
])

# Stride for the convolution
stride = 2

# Calculate the size of the activation map
activation_map_size = (
    ((image_matrix.shape[0] - conv_filter.shape[0]) // stride) + 1,
    ((image_matrix.shape[1] - conv_filter.shape[1]) // stride) + 1
)

# Initialize the activation map with zeros
activation_map = np.zeros(activation_map_size)

# Perform the convolution operation
for i in range(0, activation_map.shape[0]):
    for j in range(0, activation_map.shape[1]):
        # Extract the current region of interest in the image matrix
        region = image_matrix[i*stride:i*stride+conv_filter.shape[0], j*stride:j*stride+conv_filter.shape[1]]
        # Apply the convolutional filter (element-wise multiplication and sum)
        activation_map[i, j] = np.sum(region * conv_filter)

activation_map_size, activation_map

print(activation_map_size, activation_map)
