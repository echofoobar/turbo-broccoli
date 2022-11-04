from PIL import Image
import numpy
import sys, os
import matplotlib.pyplot as plt
from scipy import sparse


for filename in os.scandir("tiff_images"):
    if filename.path.endswith(".tif"):
        print(filename.name)
        im = Image.open(filename.path)
        imarray = numpy.array(im)
        numpy.set_printoptions(threshold=sys.maxsize,linewidth=230)
        bsr_matr = sparse.bsr_matrix(imarray.astype(int))
        bsr_matr.maxprint = bsr_matr.count_nonzero()
        f = open("processed/"+filename.name+"_bsr.txt", "w")
        f.write(str(bsr_matr))
        f.close()
        f = open("processed/"+filename.name+"_arr.txt", "w")
        f.write(str(imarray.astype(int)))
        f.close()

