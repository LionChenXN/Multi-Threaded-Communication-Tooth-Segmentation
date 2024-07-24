"""
Author: Xinning Chen
Finished Time: 24-7-2024
Function: Some initialization data and some parameters (You can modify them as you please)
"""

SEPARATOR = '@@@@'.encode()

SIZE_SEP = len(SEPARATOR)

SIZE_BYTE = 2**10

SEP_RECV = '@'.encode()

SIZE_SEP_RECV = len(SEP_RECV)

SIZE_BYTE_RECV = 10

NUM_FRAME = 8

FIN = '$_$'.encode()

SIZE_FIN = len(FIN)

DATA_PATH = r'E:\Code\PycharmProject\Practice\Multi-threaded-communication-main2\data2'

MODEL_PATH = r'E:\Code\PycharmProject\Project\model\sam_vit_h_4b8939.pth'

RES_PATH = r'E:\Code\PycharmProject\Practice\Multi-threaded-communication-main2\result'

LOG_PATH = 'E:\Code\PycharmProject\Practice\Multi-threaded-communication-main2\log'
