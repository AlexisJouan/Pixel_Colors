# This code is used to change an image in black and white into black and grey
# You will need the package pillow (PIL)

from PIL import Image

#im.show()

def load_image(name):
	im = Image.open(name)
	print(im.format, im.size, im.mode) #show properties of the picture
	return im

# Choose dose intensity by type of grey in the RGBA format (N, N, N, 255):


# Create the pixel map
def change_dose(name, intensity):
	im = load_image(name)

	pixels = im.load() 

	N = int(255*intensity)

	for i in range(im.size[0]): 
	    for j in range(im.size[1]):
	       
	        if pixels[i,j] != (0, 0, 0, 255):
	            # Change each pixel if they are not black
	            pixels[i,j] = (N, N, N, 255)
	
	im.save('intensity_'+str(intensity)+'.png')

	return pixels

change_dose('fluxonium_v0.png', 0.7)




            
