# Parts which come from other sources

- *.py: I discussed with [M. Aufi R](https://github.com/parampaa2) about the function [transform], in particular of whether I should use

```res[new_XY[0], new_XY[1]] = img[xx,yy]```

or

```res[xx,yy] = img[new_XY[0], new_XY[1]]```

To transform the image correctly, in which *img* are the original image, *xx* and *yy* are the old coordinates, and *new_XY* are the new coordinates. We went with the 1st choice.

- *.py: The matrix generation ([get_rotation], [get_scaling], [get_translation]) comes from: https://towardsdatascience.com/image-geometric-transformation-in-numpy-and-opencv-936f5cd1d315

- projectives.py: The idea of function [search_4_variables] comes from: https://math.stackexchange.com/questions/494238/how-to-compute-homography-matrix-h-from-corresponding-points-2d-2d-planar-homog
I only converted it to the form of python code

- *.py: The plotting of each image (subplots and whatnot) comes from: https://stackoverflow.com/questions/41793931/plotting-images-side-by-side-using-matplotlib Because I forgot how to plot side-by-side correctly.

# Parts I wrote myself

- I declare that every part of the code not listed above, I wrote it myself.

- The only library used are numpy, PIL.Image, and matplotlib. Numpy is used as basic array/matrix manipulation. In which, the only particular shortcut I took were np.linalg.inv() to inverse a matrix.
