import os
import cv2
import numpy as np
from PIL import Image
    
    
def check_images(directory):
    corrupted_images = 0
    valid_images = 0
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"): 
            try:
                img = Image.open(os.path.join(directory, filename)) 
                img.verify() 
                img = cv2.imread(os.path.join(directory, filename))
                if np.isnan(np.sum(img)):
                    print('Bad file:', filename)
                    corrupted_images += 1
                else:
                    valid_images += 1
            except (IOError, SyntaxError) as e:
                print('Bad file:', filename) 
                
    print(f"Corrupted Images: {corrupted_images} \n Valid Images: {valid_images}")

check_images('../datasets/Spade_ds2/images')