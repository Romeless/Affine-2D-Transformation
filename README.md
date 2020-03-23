# Sistem Pakar Assignment 1 Task 1
Rama Lesmana

1313617011

State University of Jakarta

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
