import os
import cv2
import shutil
import argparse
import numpy as np
from collections import OrderedDict

parser = argparse.ArgumentParser()
parser.add_argument('--images_path', type=str, help="path of folder containing images to run detection on.")
parser.add_argument('--dest_path', type=str, help="path of empty folder to move empty images to.")
FLAGS = parser.parse_args()

# images_path = '/home/ashimag/share_iiit_raw_autoseg_testing_24-8-2022/'
# dest_path = '/home/ashimag/empty_files/'

if not os.path.exists(FLAGS.dest_path):
	print("Empty folder path didn't existed. I have created one for you!")
	os.makedirs(FLAGS.dest_path)

image_names = os.listdir(FLAGS.images_path)
cnt = 0
empty_count = 0
for image in image_names:
	try:
		file_path = os.path.join(FLAGS.images_path, image)
		img = cv2.imread(file_path)
		cv2.imwrite(file_path, img)
		cnt = cnt + 1
		print(cnt)
	except:
		empty_count = empty_count + 1
		print(file_path)
		shutil.move(file_path, FLAGS.dest_path)

print("Total empty images found are {} and now moved to {} folder".format(empty_count, FLAGS.dest_path))