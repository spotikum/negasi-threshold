import matplotlib.image as img
from PIL import Image
import matplotlib.image as img
img = Image.open("image.jpg")

horizontal = img.size[0]-1
vertikal = img.size[1]-1

print("Ukuran Pixel = ",  horizontal, "X", vertikal)
print("Nilai Matriks =")
nilaix = 0
nilaiy = 0
for x in range(0, img.size[0]-1):
     nilaix = nilaix + 1

     for y in range(0, img.size[1]-1):
          if nilaiy >= vertikal:
               nilaiy = 1
          else:
               nilaiy = nilaiy + 1
          
          pixelColorVals = img.getpixel((x,y))
          print("x", nilaix)
          print("y", nilaiy)
          print(pixelColorVals)

          redPixel    = 255 - pixelColorVals[0]; 

          greenPixel  = 255 - pixelColorVals[1]; 

          bluePixel   = 255 - pixelColorVals[2]; 

          print("Nilai Red = ", redPixel)
          print("Nilai Green= ", greenPixel)
          print("Nilai Blue = ", bluePixel)

          img.putpixel((x,y),(redPixel, greenPixel, bluePixel))

img.save('output.png')