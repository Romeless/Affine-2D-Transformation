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
![Perspective](/img/sample_project.jpg)

