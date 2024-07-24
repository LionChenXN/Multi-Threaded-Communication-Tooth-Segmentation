from client.my_client import *
from client.get_img import *
import threading
import queue
from utils.constants import *

"""
Author: Xinning Chen
Finished Time: 24-7-2024
Function: Obtain tooth segmentation results in the form of producers and consumers
"""

# Message queue
img_queue = queue.Queue()

# Create Producer
producers = []
# for k, v in urls.items():
    # producers.append(threading.Thread(target=get_img, args=(k, v, img_queue,)))
producers.append(threading.Thread(target=get_img, args=(img_queue,)))
for producer in producers:
    producer.start()

# Create Consumer
consumer = threading.Thread(target=operation, args=(img_queue,))
consumer.start()

for producer in producers:
    producer.join()

# Sends the end signal to the consumer thread
img_queue.put('FIN')

consumer.join()