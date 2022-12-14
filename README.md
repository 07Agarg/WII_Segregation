# WII_Segregation

### Steps To Run Detection On Wildlife Images: 

1. To remove corrupt error issue with images and move empty files to a different location, run ```cv2_load_save.py``` file. Set images_directory path to ```--images_path``` argument and empty_folder path to ```--dest_path``` where the empty files will be moved to. 
Command to run this file is following :  <br />
```python cv2_load_save.py --images_path 'D:\images_directory\site0001' --dest_path 'D:\empty_folder'    ```



2. To run detection on images_directory, run the following command: <br />
```bash 
python detect.py --source 'D:\images_directory\site0001'                             ### path to directory containing images (Note: Step 1 should be already completed.)
                 --weights runs/train/wii_28_072/weights/best.pt                     ### path to model weights.
                 --data data/wii_aite_2022_testing.yaml                              ### path to yaml file containing species names 
                 --img 640                                                           ### image size 
                 --save-txt                                                          ### save label txt files for every image.  
                 --save-conf                                                         ### saves confidences in label txt files.  
                 --name yolo_test_24_08_site0001                                     ### folder name created in ```runs/detect/``` with labels  
                 --conf-thres 0.001                                                  ### confidence threshold 0.001
                 --iou-thres 0.6                                                     ### iou_threshold 0.6
```
Arguments to change to run on different image directory includes : ```--source``` and ```--name```. 



3. To create tags of the images with the generated labels, run tag_images.py. 
```bash
python tag_images.py --images_path 'D:\images_directory\site0001'                    ### path to images for testing
                     --pred_path 'runs/detect/yolo_test_24_08_site0001/labels/'      ### path where label .txt file is stored
                     --tagged_path 'D:\images_directory\site0001_tagged'             ### path where tagged images will be stored
```



