from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#plotting object with 2 subplots
fig, axs = plt.subplots(2)

# images
im = dict()

# the image we're transforming
im['og'] = Image.open('./PontNeuf.jpg')
im['tf1'] = im['og']

axs[0].imshow(im['og'])
axs[1].imshow(im['tf1'])
plt.show()
