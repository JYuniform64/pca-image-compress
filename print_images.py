# This is used to view all images in a folder from dataset
import pgm
import os
import sys
import numpy as np
from PIL import Image

def saveImage(matrix, filename, saveFormat):
    folder = "view"
    os.makedirs(folder, exist_ok=True)
    img = Image.fromarray(matrix).convert('L')
    filename = filename.split('.')[0] + '.' + saveFormat
    filename = os.path.join(folder, filename)
    img.save(filename, saveFormat)

def viewImagesInFolder(folder, dataFormat = 'pgm', saveFormat = 'png'):
    images = [file for file in os.listdir(folder) if file.endswith(dataFormat)]
    for image in images:
        with open(os.path.join(folder, image), 'rb') as pgmf:
            mat = pgm.read_pgm(pgmf)
            saveImage(mat, image, saveFormat)

if __name__ == '__main__':
    folder = sys.argv[1]
    viewImagesInFolder(folder)