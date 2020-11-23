import numpy as np
from sklearn.decomposition import PCA

from PIL import Image

import os
import sys
import pgm
import argparse


def error(data, recdata):
    sum1 = 0
    sum2 = 0
    # 计算两幅图像之间的差值矩阵
    D_value = data - recdata
    # 计算两幅图像之间的误差率，即信息丢失率
    for i in range(data.shape[0]):
        sum1 += np.dot(data[i], data[i])
        sum2 += np.dot(D_value[i], D_value[i])
    error = sum2/sum1
    print(sum2, sum1, error)


def showImage(matrix):
    img = Image.fromarray(matrix)
    img.show()


def saveImage(matrix, form, pgmFileName, dimension):
    folder = 'image'
    os.makedirs(folder, exist_ok=True)
    img = Image.fromarray(matrix).convert('L')
    filename = pgmFileName.split(
        '\\')[-1].split('.')[0] + '_d_' + str(dimension) + '.' + form
    filename = os.path.join(os.getcwd(), folder, filename)
    print('image saved at ' + filename)
    img.save(filename, form)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pgmFile", help="the pgm image to be compressed")
    parser.add_argument("-q", "--quite", action="store_true",
                        help="compress the image without displaying")
    parser.add_argument("-s", "--save", type=str,
                        help="save the compressed image as designated format")
    parser.add_argument("-n", "--num", type=int,
                        help="the number of dimension to retain, default is 10")
    args = parser.parse_args()

    with open(args.pgmFile, 'rb') as pgmf:
        data = pgm.read_pgm(pgmf)
    dim = args.num if args.num else 10
    pca = PCA(n_components=dim).fit(data)
    x_new = pca.transform(data)
    recdata = pca.inverse_transform(x_new)
    # error(data, recdata)
    if not args.quite:
        showImage(recdata)
    if args.save:
        saveImage(recdata, args.save, args.pgmFile, args.num)
