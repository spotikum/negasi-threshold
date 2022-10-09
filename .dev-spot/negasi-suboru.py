# using matplotlib and numpy
#import cv2
import matplotlib.image as img
import numpy as npy

from PIL import Image

from PIL import ImageFilter

import matplotlib.image as img
import numpy as npy

# provide the location of image for reading
##m = img.imread("tes.PNG");
#imgs = cv2.imread('tes.PNG',cv2.IMREAD_UNCHANGED)
# determining the length of original image
#w, h = m.shape[:2];

# xNew and yNew are new width and
# height of image required
#after scaling
#xNew = int(w * 1 / 2);
#yNew = int(h * 1 / 2);

# calculating the scaling factor
# work for more than 2 pixel
#xScale = xNew/(w-1);
#yScale = yNew/(h-1);

# using numpy taking a matrix of xNew
# width and yNew height with
# 4 attribute [alpha, B, G, B] values
#iamges = npy.zeros([xNew, yNew, 4]);
#newImage = 255 - m
#imgsproses = 255 - imgs
#for i in range(xNew-1):
#    for j in range(yNew-1):
#	    newImage[i + 1, j + 1]= m[1 + int(i / xScale),
#								1 + int(j / yScale)]

# Save the image after scaling
#img.imsave('scaled.png', newImage);
##print (imgsproses)
#img.imsave('scaled.png', imgsproses);


 



img = Image.open(".dev-spot/image.jpeg");

#print(img)
 
for i in range(0, img.size[0]-1):

    for j in range(0, img.size[1]-1):




        pixelColorVals = img.getpixel((i,j));

       
        #print(pixelColorVals)


        redPixel    = 255 - pixelColorVals[0]; 

        greenPixel  = 255 - pixelColorVals[1]; 

        bluePixel   = 255 - pixelColorVals[2]; 

                   
        #print(redPixel)
        #print(greenPixel)
        #print(bluePixel)


        img.putpixel((i,j),(redPixel, greenPixel, bluePixel));

 


img.save('output.png');



#import cv2
#img = cv2.imread('tes.PNG', )#cv2.IMREAD_UNCHANGED)
#print  (img)

#import cv2
#import numpy as np
# Load the image
#img = cv2.imread('tes.PNG',cv2.IMREAD_UNCHANGED)
# Check the datatype of the image
#print(img.dtype)
# Subtract the img from max value(calculated from dtype)
#img_neg = 255 - img
# Show the image
#cv2.imshow('asu',img_neg)
#cv2.waitKey(0)
#print(img_neg)