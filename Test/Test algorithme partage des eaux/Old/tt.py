import numpy as np
from PIL import Image

array = np.zeros([100, 200], dtype=np.uint8)

# Set grey value to black or white depending on x position

for x in range(200):
    for y in range(100):
        if (x % 16) // 8 == (y % 16) // 8:
            array[y, x] = 255
        else:
            array[y, x] = 255

print(array)
img = Image.fromarray(array)
img.save('testgrey.png')
