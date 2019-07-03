from PIL import Image
import sys

def resizeImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_img = image.resize((width, height), Image.ANTIALIAS)
    resized_img.save(file_out)

if __name__ == '__main__':

    status = 1
    if len(sys.argv) != 4:
        print("\nUsage: python resize.py FILENAME WIDTH HEIGHT\n")
        status = 0

    if status == 1:
        file_in = sys.argv[1]
        width = int(sys.argv[2])
        height = int(sys.argv[3])
        file_out = sys.argv[2] + sys.argv[3] + '_' + file_in

        resizeImage(file_in, width, height, file_out)
