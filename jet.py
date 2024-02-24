import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('', cv2.IMREAD_GRAYSCALE)

cmap = plt.get_cmap('jet')

normalized_image = cv2.normalize(image, None, 0, 1, cv2.NORM_MINMAX)

pseudo_color_image = (cmap(normalized_image) * 255).astype(np.uint8)

plt.subplot(121)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(122)
plt.title('Pseudo-Colored Image')
plt.imshow(pseudo_color_image)

plt.show()
