import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r'', cv2.IMREAD_GRAYSCALE)

cmap = plt.get_cmap('hot')

min_intensity = 0  
max_intensity = 255  
normalized_image = (image - min_intensity) / (max_intensity - min_intensity)

pseudo_color_image = (cmap(normalized_image) * 255).astype(np.uint8)

plt.subplot(121)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(122)
plt.title('Pseudo-Colored Image')
plt.imshow(pseudo_color_image)

plt.show()
