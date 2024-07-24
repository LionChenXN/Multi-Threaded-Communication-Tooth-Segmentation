import requests
import re
from bs4 import BeautifulSoup
import queue
from utils.constants import *
import os

"""
Author: Xinning Chen
Finished Time: 24-7-2024
Function: Load 2D tooth image from local
"""

# Load 2D tooth image from local
def get_img(img_queue: queue.Queue):
    path = DATA_PATH
    if not os.path.exists(path):
        os.makedirs(path)
    names = os.listdir(path)

    for name in names:
        pic_path = path+f'/{name}'
        img_queue.put(pic_path)



if __name__ == '__main__':
    for k, v in urls.items():
        pass
    img_queue = queue.Queue()
    get_img(img_queue)

