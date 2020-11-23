# PCA image compression
----------------------------------------------------------------

A simple program to compress `.pgm` image using PCA.
For me it is used in Yale Face Database, mainly for study purposes.

## usage

compress.py
```
usage: python compress.py [-h] [-q] [-s SAVE] [-n NUM] pgmFile

positional arguments:
  pgmFile               the pgm image to be compressed

optional arguments:
  -h, --help            show this help message and exit
  -q, --quite           compress the image without displaying
  -s SAVE, --save SAVE  save the compressed image as designated format
  -n NUM, --num NUM     the number of dimension to retain, default is 10
  
```

print_images.py
```
It is used to print all images in a subfolder of the dataset. Images will be shown at view/ .

usage: python print_images.py subFolder
```

joint_image.py
```
It is used to joint images in images/ for comparison.

usage: python joint_image.py
```

generate_image.bat
```
It is used to generate compressed images from dimension 1 to n.

usages: ./generate_image.bat pgmFile n
```