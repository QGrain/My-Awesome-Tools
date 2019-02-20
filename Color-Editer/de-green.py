
from PIL import Image
import sys

if (len(sys.argv) == 1):
    initial_name = 'green_cat.jpg'
elif (len(sys.argv) == 2):
    initial_name = sys.argv[1]
new_name_prefix = 'degreen_cat'
name_version = ['-10', '-20', '-30']
new_name_suffix = '.jpg'
scale = 10

img = Image.open(initial_name)
img_array = img.load()
print ('imgsize:', img.size)

width, height = img.size
for version in name_version:
    scale = scale + 10
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img_array[x, y]
            b_new = b + scale
            img_array[x, y] = r, g, b_new
    img.save(new_name_prefix + version + new_name_suffix)


