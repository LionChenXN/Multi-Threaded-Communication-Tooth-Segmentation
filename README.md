# Multi-Threaded-Communication-Tooth-Segmentation
2D Intraoral Scanning Image Dental Segmentation via SAM Based on Multi-threaded Communication Network

## Function
Image transmission and tooth segmentation <br />
<br />
![image](https://github.com/user-attachments/assets/6688be18-c0f6-49ba-b886-ce47a6a1ff3d)


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

## Data
https://zoubo9034.github.io/TeethSEG/

## References
* Zou B, Wang S, Liu H, et al. Teeth-SEG: An Efficient Instance Segmentation Framework for Orthodontic Treatment based on Multi-Scale Aggregation and Anthropic Prior Knowledge[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024: 11601-11610.
* Kirillov A, Mintun E, Ravi N, et al. Segment anything[C]//Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023: 4015-4026.

