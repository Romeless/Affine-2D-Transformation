# Sistem Pakar Assignment 1 Task 1
#### Rama Lesmana
#### 1313617011
#### State University of Jakarta



My solution to Task 1 of Assignment 1 from class "Sistem Pakar".
This task involves the transformation of Image in the form of 2D Arrays.

Python is the chosen programming language used to replicate the transformation of the 2D array.

## Affine Transformation
The transformation included in this task are:
1. Scaling
2. Rotation
3. Translation
4. Projectives

The first 3 out of the transformation are similar to the other, especially since the homography matrix are already included in the module and are easily searchable on the net.

### Original Image
![Original](/img/sample.jpg)

### Scaling
![Scaling](/img/sample_scale.jpg) 
![Scaling](/img/sample_scale2.jpg) 

Scaling involves the transformation matrix:
```
[scale_x, 0, 0]
[0, scale_y, 0]
[0,       0, 1]
```

### Rotation
![Rotation](/img/sample_rotate.jpg)

Rotation involves the transformation matrix:
```
[cos(a), -sin(a), 0]
[sin(a),  cos(a), 0]
[     0,       0, 1]
Where a is the angle of rotation
``` 

### Translation
![Translation](/img/sample_translate.jpg)

Translate involves the transformation matrix:
```
[ 0, 0, tx]
[ 0, 0, ty]
[ 0, 0,  1]
Where a is the angle of rotation
```

### Projectives
![Perspective](/img/sample_project1.jpg)

Projective is a lot trickier than the previous 3 transformation, due to the sheer freedom its matrix give. To correctly project the Image, at least 4 pair of initial coordinates and final coordinates is needed. In the end of the transformation, the initial coordinates will be placed on its pairing final coordinates.

The module includes how to calculate the matrix elements:
```
[ h00, h01, h02]
[ h10, h11, h12]
[ h20, h21, h22]
Where h22 is usually 1

x' = (h00 * x + h01 * y + h02) / (h20 * x + h21 * y + h22)
y' = (h10 * x + h11 * y + h12) / (h20 * x + h21 * y + h22)
Where (x,y) is the initial coordinates and (x',y') is the final coordinates
```
However I have a hard time figuring out how to turn it into a code. However, following [this article](https://math.stackexchange.com/questions/494238/how-to-compute-homography-matrix-h-from-corresponding-points-2d-2d-planar-homog), I managed to write a python code of how to calculate the matrix element given the initial coordinates and final coordinates.

## How they are translated to code
For the most part, the code's backbone lies in the [transform] function. This function, given the image array and the transformation matrix, will return the resulting image.

The basic of the code is:
```
for each ROW in IMAGE:
  for each COL in IMAGE:
    new_ROW, new_COL, i = TRANSFORMATION_MATRIX @ [ROW, COL, 1]
    
    new_IMAGE[new_ROW, new_COL] = IMAGE[ROW, COL]
return new_IMAGE
```

The point of this code is to get the homography coordinate of the image one by one, and then dot product said coordinate with the transformation matrix. The resulting coordinate is where the previous coordinate's color/pixel should be.

## Interesting things I found while experimenting
There's one thing I found interesting in this experiment. Looking through the images above such as scaling and rotation, one may notice the black spots inbetween the image. This is caused by the nature of the code, which is:
```
#from the function transform
for xx in range(row):
  for yy in range(column):
    ...
    res[new_XY[0], new_XY[1]] = img[xx,yy]
    ...
```
Since this code loop through pixel per pixel in the form of *xx* and *yy*, while the resulting image uses the new coordinates from the result of transformation matrix dot product *xx* and *yy*, there's bound to be some pixel where the new coordinate do not go through. Meanwhile, the code
```
res[xx,yy] = img[new_XY[0], new_XY[1]]
```
results in a near-perfect, no black spots in the image. The problem of this method is, the new coordinates are wrong, it's mirrored. For example, scaling the image by 2 will cut it in half (0.5) instead.

![Scaling Method 1](/img/sample_scale_right.jpg) 
![Scaling Method 2](/img/sample_scale_wrong.jpg)

The left image is the result of scaling by 2 with code 1. The right image is the result of scaling by 0.5 with code 2.
Obviously, when scaling the image by 2, the image should look bigger, and while scaling by 0.5 the image should look smaller.
This isn't the case for method 2, where the result looks like what the left should look like.

How to fix this confuses me for a while, until I discuss it with a [fellow classmate](https://github.com/parampaa2) which method is more right. From what we briefly discuss, the left method is correct, and to fix it several other implementation like anti-aliasing should be used. Which I haven't yet implemented.
