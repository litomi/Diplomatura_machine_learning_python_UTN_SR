import matplotlib.pyplot as plt
import numpy as np

# Create some NumPy arrays
images = [np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
          np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]]),
          np.array([[20, 21, 22], [23, 24, 25], [26, 27, 28]])]

# Plot the images
for i in range(len(images)):
  plt.subplot(1, len(images), i + 1)
  plt.imshow(images[i])
  plt.title("Image {}".format(i + 1))

# Show the plot
plt.show()
