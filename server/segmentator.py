import os
import cv2
import numpy as np
import random
import torch
from segment_anything import SamPredictor, SamAutomaticMaskGenerator, sam_model_registry
from utils.constants import *

"""
Author: Xinning Chen
Finished Time: 24-7-2024
Notice: 
    (1) You need to download the model checkpoint of Segment Anything(SAM) and place it at the relevant address for inference.
    (2) The website of SAM: https://github.com/facebookresearch/segment-anything#model-checkpoints
"""

# Random Generation of Mask Colours
def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (b, g, r)

# Model Load
def model_load(model_path):
    sam = sam_model_registry["vit_h"](checkpoint=model_path)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    sam = sam.to(device)

    return sam

# Mask Generation and Splicing
def get_res(image):

    sam = model_load(MODEL_PATH)

    mask_generator = SamAutomaticMaskGenerator(sam)
    masks = mask_generator.generate(image)

    mask_colors = []
    for i, mask in enumerate(masks):
        mask_array = mask['segmentation']
        mask_rgb = np.zeros_like(image)
        mask_rgb[:, :, 0] = mask_array * 255
        mask_rgb[:, :, 1] = mask_array * 255
        mask_rgb[:, :, 2] = mask_array * 255

        color = generate_random_color()

        mask_colors.append((color, mask_array))

    output_image = image.copy()
    for color, mask_array in mask_colors:
        output_image[mask_array > 0] = color


    return output_image

if __name__ == '__main__':
    import time, datetime
    image_path = r"../data/Mesh1.jpg"
    image = cv2.imread(image_path)
    output_path = r"../output5"
    os.makedirs(output_path, exist_ok=True)
    output_image_path = r"../output5/test2_combined_image.png"
    start_time = time.time()
    get_res(image, output_image_path)
    end_time = time.time()
    print(datetime.timedelta(seconds=(end_time - start_time)))


