from __future__ import print_function
import os

from PIL import Image



#files = ['1.jpg','2.jpg','3.jpg','4.jpg']

result = Image.new("RGB", (1200, 2000))

def save_image(val,files):
	for index, file in enumerate(files):
		path = os.path.expanduser(file)
		img = Image.open(path)
		img.thumbnail((400, 400), Image.ANTIALIAS)
		w, h = img.size
		if index % 2 ==0:
			x=100
			y = (int(index/2)+1)*300 
		else:
			x=700
			y = (int(index/2)+1)*300 
		result.paste(img, (x, y, x + w, y + h))

	result.save(os.path.expanduser('~/result/image{}.jpg'.format(val)))

files = [str(i+1)+".jpg" for i in range(220)]
for i in range(22):
	save_image(i,files[i*10:i*10+10])
