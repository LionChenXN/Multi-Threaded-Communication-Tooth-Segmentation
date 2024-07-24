import socket
import cv2
from utils.constants import *
import numpy as np
import queue
import os
from utils.get_log import GetLogger

"""
Author: Xinning Chen
Finished Time: 24-7-2024
Function: The client sends and receives data
"""

print_log = GetLogger.get_logger()


def client(ip_port, img=None):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # s.setblocking(False)
    s.connect(ip_port)

    if img is None:
        s.send(FIN)

    while img is not None:
        """
            send an image
        """
        # Encodes the image and transmits it to the server as a stream of bytes
        img_encode = cv2.imencode('.jpg', img)[1]
        img_bytes = img_encode.tobytes()

        size = len(img_bytes)
        num_seg = size // 1024
        num_remain = size % 1024

        print_log.info("Sending img ...")
        for i in range(num_seg):
            start, end = i * 1024, (i + 1) * 1024
            s.send(img_bytes[start:end])
        s.send(img_bytes[-num_remain:] + SEPARATOR + b'\n' * (1024 - num_remain - SIZE_SEP))
        print_log.info("Sending img done ...")

        res = s.recv(SIZE_BYTE)
        while SEP_RECV not in res:
            res = s.recv(SIZE_BYTE)

        if SEP_RECV in res:
            break

    s.close()


def start_listen(pic):
    ip_port = ('10.16.49.100', 5900)
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sk.bind(ip_port)
    sk.listen()

    data = b''  # init for an image byte stream
    print_log.info("Getting result img_{}...".format(pic))
    conn, address = sk.accept()
    while True:
        # Parsing an image byte stream
        temp = conn.recv(SIZE_BYTE)
        if SEPARATOR not in temp:
            data += temp
        if SEPARATOR in temp:
            f = temp.find(SEPARATOR)
            data += temp[:f]
            img_encode = np.frombuffer(data, dtype=np.uint8)
            img = cv2.imdecode(img_encode, 1)
            if not os.path.exists(RES_PATH):
                os.makedirs(RES_PATH)
            cv2.imwrite(RES_PATH + '/' + "{}".format(pic), img)
            conn.send(SEP_RECV)
            break

    sk.close()


def operation(img_queue: queue.Queue):
    while True:
        ip_port = ('10.16.74.196', 5800)
        path = img_queue.get()
        if path == 'FIN':
            client(ip_port, None)
            print_log.info('Finish...')
            break
        img = cv2.imread(path)
        print_log.info(f'reading img of {path}')
        if img is None:
            print_log.info('Skipping this invalid images')
            print_log.info("Continue...")
            continue
        pic_name = path.split(r'/')[-1]
        client(ip_port, img)
        start_listen(pic_name)
        print_log.info("Continue...")
