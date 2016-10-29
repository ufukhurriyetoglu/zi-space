import numpy as np
import os
from scipy import ndimage
from six.moves import cPickle as pickle

image_size = 44
pixel_depth = 255.0
data_folder = 'simp_jhenghei' 

images = os.listdir(data_folder)
data = np.ndarray(shape=(len(images), image_size, image_size), dtype = np.float32)

img_index = 0

for image in images:
	if image.endswith('.png'):
		image_file = os.path.join(data_folder, image)
		image_data = (ndimage.imread(image_file).astype(float) - 
				                    pixel_depth / 2) / pixel_depth
		greyscale_data = np.sum(image_data, 2) / 3
		data[img_index, :] = np.reshape(greyscale_data, (1, image_size, image_size)) 
		img_index += 1

with open(data_folder + '.pickle', 'wb') as f:
	pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
	
