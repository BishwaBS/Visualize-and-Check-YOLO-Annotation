import os
import glob
import PIL.Image as Image
import numpy as np
import cv2
import matplotlib.pyplot as plt

##Note: Please make sure that the "imagedir" contains both images and text file for each image together

def check_annotations(imagedir):

    #setup the directory provided by the user as the current working directory
    os.chdir(imagedir)
    plt.rcParams["keymap.quit"] = ['ctrl+w', 'cmd+w', ' ']

    #iterating over every images in dir
    for file in glob.glob("*.JPG"):
        plt.figure(figsize=(15, 15))
        image=Image.open(file)
        image=np.array(image)
        size=image.shape[0]
        textfile=file.rsplit(".", 1)[0] + ".txt"

        #checking if the textfile for the respective image exists
        if os.path.exists(textfile):
            #iterating over each line in the text file
            for line in open(textfile):
                splits=line.split()
                x, y, w, h= float(splits[1]), float(splits[2]), float(splits[3]), float(splits[4])
                x1, y1 = int((x - w / 2)* size), int((y - h / 2)*size)
                x2, y2 = int((x + w / 2)*size), int((y + h / 2)*size)
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 3)
                cv2.putText(image, splits[0],(x1, y1-20),cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)

            plt.imshow(image)
            plt.title(file.rsplit(".", 1)[0])
            plt.show()

        else:
            print ("{} does not exists".format(textfile))
            continue

#check_annotations(r"J:\Research\images")