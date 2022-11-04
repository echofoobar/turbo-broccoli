# Quantitative analysis

We used CT-scan images from TCIA Archive. 
#### Data Citation
```
Albertina, B., Watson, M., Holback, C., Jarosz, R., Kirk, S., Lee, Y., Rieger-Christ, K., & Lemmerman, J. (2016). The Cancer Genome Atlas Lung Adenocarcinoma Collection (TCGA-LUAD) (Version 4) [Data set]. The Cancer Imaging Archive. https://doi.org/10.7937/K9/TCIA.2016.JGNIHEP5
```
#### TCIA Citation
```
Clark, K., Vendt, B., Smith, K., Freymann, J., Kirby, J., Koppel, P., Moore, S., Phillips, S., Maffitt, D., Pringle, M., Tarbox, L., & Prior, F. (2013). The Cancer Imaging Archive (TCIA): Maintaining and Operating a Public Information Repository. In Journal of Digital Imaging (Vol. 26, Issue 6, pp. 1045–1057). Springer Science and Business Media LLC. https://doi.org/10.1007/s10278-013-9622-7
```

## Preprocessing

- First 32bit .tiff images were converted to 1bit .tiff images as for our research we are interested only in binary type of matrices. Conversion happened with command `magick mogrify -format tif -depth 1 *.tif`
in the correct folder.  
- Next we generated matrices from these tiff images with python. In these matrices zero represents black pixel and one white pixel.

## Independent and dependent variables

- With python we also generated preliminary matrix conversion to Block Storage Format
- In our research our independent variables are the matrices generated from CT-scan images and dependent variables are the sizes of the matrices in the Block Storage Row format.
- - As the CT-scan images have same amount of pixels 512x512, only property here are the black and white pixels.
- - For the matrix storage format we are interested in the pixels that are important to store and therefore interesting properties for dependent variable are the space and time the storage format requires.

## Exploratory analysis

- With exploratory data anaylsis we were investigating if the images and generated sparse matrices contain dense sub-matrices. This was done with python and if CT-scan contains dense submatrix, program will just simply print 'True' to stdout. The check was done by first creating new matrix of sum of every neighboring (3 elements every direction) elements and this "neighbor_sum_matrix" was then transformed to array by summing every element in each row. Finally it was checked that if in this array there is at least one row with only zeroes (the sum is 0) and at least one row with sum value higher than 512 (this was chosen by comparing the results).



 
