import numpy as np
import matplotlib.image as mpimg


# take two images with same camera with distance of your eyes
# and combine to create 3D stereoscopic image
# it works :)
def combineTo3D(im1,im2):
  width = im1.shape[0]
  height = im1.shape[1]
  new = np.array(im1)

  for i in range(width):
    for j in range(height):
      pixel1 = im1[i][j]
      pixel2 = im2[i][j]

      red1 =   pixel1[0]
      green1 = pixel1[1]
      blue1 =  pixel1[2]

      red2 =   pixel2[0]
      green2 = pixel2[1]
      blue2 =  pixel2[2]

      gray1 = (red1 * 0.299) + (green1 * 0.587) + (blue1 * 0.114)
      gray2 = (red2 * 0.299) + (green2 * 0.587) + (blue2 * 0.114)

      new[i][j][0] = int(gray2)
      new[i][j][1] = int(gray1)
      new[i][j][2] = int(gray1)

  return new

img1=mpimg.imread('IMG_1413.jpg')
img2=mpimg.imread('IMG_1414.jpg')
imF = combineTo3D(img1,img2)
mpimg.imsave("final.jpg", imF)

