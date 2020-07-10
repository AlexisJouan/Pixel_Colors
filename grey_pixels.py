
'''This very simple code is used to change an image in black and white into black and grey
You will need the package pillow (PIL)
Choose dose intensity by type of grey in the RGBA format (N, N, N, 255) where N = int(255*intensity)
Alexis Jouan - 01/06/2020'''

#=== Import library ===#

from PIL import Image
import sys
import zipfile as zp
import numpy as np

#=== Arguments ===#

#1. name (string) 2. format (string) 3. intensity (float)

args = sys.argv

folder = args[1]
filename = args[2]

#=== Functions ===#

def load_image(name):
	im = Image.open(name)
	print(im.format, im.size, im.mode) #show properties of the picture
	#im.show()
	return im

def change_dose(file, intensity):
	#file_name = name+'.'+file_format
	#Load image
	im = load_image(file)

	# Create the pixel map
	pixels = im.load() 
	new_pixels = np.zeros((im.size[1], im.size[0], 4), dtype='|u1')

	N = int(255.0*intensity)

	for i in range(im.size[0]): 
	    for j in range(im.size[1]):
	        
	        (r, g, b, a) = pixels[i,j]
	        # Change each pixel 
	        new_pixels[j,i] = (int(r*intensity), int(g*intensity), int(b*intensity), a)
	
	#im.save(name+'_intensity_'+str(intensity)+'.'+file_format)

	return new_pixels


if __name__ == "__main__":
	png_nbs =[]
	doses = []
	png_nbs = [int(item) for item in input("Enter write-field numbers : ").split()]
	doses = [float(item) for item in input("Enter corresponding doses : ").split()]

	png_new = []

	with zp.ZipFile(folder+filename+'.stitch', 'r') as myzip:
		for png_nb, dose in zip(png_nbs, doses):
			with myzip.open(f'{png_nb}.png', 'r') as myfile:
				png_new.append(change_dose(myfile, dose))

	def condition(string, elements):
		return string not in [str(e)+'.png' for e in elements]

	zin = zp.ZipFile (folder+filename+'.stitch', 'r')
	zout = zp.ZipFile (folder+filename+'_out.stitch', 'w')
	
	for item in zin.infolist():
		buffer = zin.read(item.filename)
		if condition(item.filename, png_nbs):
			zout.writestr(item, buffer)
	zout.close()
	zin.close()

	with zp.ZipFile(folder+filename+'_out.stitch', 'a') as myzip:
		for png_nb, png_data in zip(png_nbs, png_new):
			with myzip.open(f'{png_nb}.png', 'w') as myfile:
				im = Image.fromarray(png_data)
				im.save(myfile, 'png')
		




            
