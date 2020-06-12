
'''This very simple code is used to change an image in black and white into black and grey
You will need the package pillow (PIL)
Choose dose intensity by type of grey in the RGBA format (N, N, N, 255) where N = int(255*intensity)
Alexis Jouan - 01/06/2020'''

#=== Import library ===#

from PIL import Image
import sys

#=== Arguments ===#

#1. name (string) 2. format (string) 3. intensity (float)

args = sys.argv

folder = args[1]
picture_format = args[2]
grey_intensity = float(args[3])

#=== Functions ===#

def load_image(name):
	im = Image.open(name)
	print(im.format, im.size, im.mode) #show properties of the picture
	#im.show()
	return im

def change_dose(name, file_format, intensity):
	file_name = name+'.'+file_format
	#Load image
	im = load_image(file_name)

	# Create the pixel map
	pixels = im.load() 

	N = int(255.0*intensity)

	for i in range(im.size[0]): 
	    for j in range(im.size[1]):
	        
	        (r, g, b, a) = pixels[i,j]
	        # Change each pixel 
	        pixels[i,j] = (int(r*intensity), int(g*intensity), int(b*intensity), a)
	
	im.save(name+'_intensity_'+str(intensity)+'.'+file_format)

	return pixels


if __name__ == "__main__":
	file_names =[]
	file_names = [int(item) for item in input("Enter the write-field numbers : ").split()]
	print(file_names)
	for file_name in file_names:
		change_dose(folder+str(file_name), picture_format, grey_intensity)




            
