# Multi-Threaded-Communication-Tooth-Segmentation
2D Intraoral Scanning Image Dental Segmentation via SAM Based on Multi-threaded Communication Network

## Function
Image transmission and tooth segmentation

## Related Technology
* Multi-Threaded
* Segment Anything (SAM)
* Tooth Segmentation
* OpenCV

## Functional Process
* The client reads tooth images from local
* The client sends images to server
* The server segments teeth in images using SAM
* The server sends the segmentation result to the client

## Useage
* Deploy the server folder to the server side, and other folder can deploy to the client side
* Run my_server.py in the server side firstly, then launch  main.py in the client side
