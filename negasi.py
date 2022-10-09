import matplotlib.image as img
from PIL import Image

img = Image.open("image.jpeg");

for i in range(0, img.size[0]-1):
     for j in range(0, img.size[1]-1):
          pixelColorVals = img.getpixel((i,j));
          redPixel    = 255 - pixelColorVals[0]; 
          greenPixel  = 255 - pixelColorVals[1]; 
          bluePixel   = 255 - pixelColorVals[2]; 
          img.putpixel((i,j),(redPixel, greenPixel, bluePixel));
img.save('output.png');