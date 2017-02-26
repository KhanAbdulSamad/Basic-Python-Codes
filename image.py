from scipy import misc
img=misc.imread('image.jpg')
print(type(img))        #numpy.ndarray
print(img.shape,img.dtype) #(4032, 3024, 3) uint8

#shrink the image down, for faster computing

img=(img/255.0).reshape(-1,3)

print(img.shape)

