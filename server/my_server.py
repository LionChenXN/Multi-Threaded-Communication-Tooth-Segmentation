import socket
import numpy as np
from server.segmentator import *
import time

"""
Author: Xinning Chen
Finished Time: 24-7-2024
Function: The code of your Server-side. Run it on your server.
"""


def start_listen(idx):

    ip_port = ('10.16.74.196', 5800)
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sk.bind(ip_port)
    sk.listen()

    data = b''  # init for an image byte stream

    print("Socket now listening...")
    conn, address = sk.accept()
    while True:
        res = None
        IFCLOSE = False
        # get the image byte stream
        temp = conn.recv(SIZE_BYTE)
        if FIN in temp:
            print('****************')
            IFCLOSE = True
            break
        if SEPARATOR not in temp:
            data += temp
        if SEPARATOR in temp:
            f = temp.find(SEPARATOR)
            data += temp[:f]
            img_encode = np.frombuffer(data, dtype=np.uint8)
            img = cv2.imdecode(img_encode, 1)

            res = get_res(img)
            print('Get img_{} result done...'.format(idx))
            cv2.imwrite('../img/{}.jpg'.format(idx), res)
            data = b''

            conn.send(SEP_RECV)
            break

    sk.close()
    return res, IFCLOSE


def client(ip_port, img):
    print('Sending res now...')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 新增
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # s.setblocking(False)
    time.sleep(2)
    s.connect(ip_port)
    while True:
        img_encode = cv2.imencode('.jpg', img)[1]
        img_bytes = img_encode.tobytes()

        size = len(img_bytes)
        num_seg = size // 1024
        num_remain = size % 1024
        for i in range(num_seg):
            start, end = i * 1024, (i+1) * 1024
            s.send(img_bytes[start:end])
        s.send(img_bytes[-num_remain:] + SEPARATOR + b'\n' * (1024-num_remain-SIZE_SEP))
        print('Sending res done...')

        res = s.recv(SIZE_BYTE)
        while SEP_RECV not in res:
            res = s.recv(SIZE_BYTE)

        if SEP_RECV in res:
            break
    s.close()


if __name__ == '__main__':
    idx = 0
    while True:
        idx += 1
        res, CLOSE = start_listen(idx)
        if CLOSE:
            print('Finished...')
            break
        ip_port = ('10.16.49.100', 5900)
        client(ip_port, res)
        print('Next...')
