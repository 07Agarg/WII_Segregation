import os
import cv2
import torch
import torchvision
import numpy as np
import shutil
from collections import OrderedDict

# val_path = '/home/ashimag/wii_data_species_2022/images/test'
val_path = '/home/ashimag/share_iiit_raw_autoseg_testing_24-8-2022/'
image_names = os.listdir(val_path)
cnt = 0
empty_count = 0
for image in image_names:
	try:
		file_path = os.path.join(val_path, image)
		img = cv2.imread(file_path)
		cv2.imwrite(file_path, img)
		cnt = cnt + 1
		print(cnt)
	except:
		empty_count = empty_count + 1
		print(file_path)
		dest_path = '/home/ashimag/empty_files/'
		shutil.move(file_path, dest_path)


print(empty_count)