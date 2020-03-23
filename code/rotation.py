#!/home/romeless/anaconda3/envs/rome/bin/python
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = np.array(Image.open("sample.jpg"))
print(img.shape)

def transform(img, A):
    res = np.zeros(img.shape)
    row, column = img.shape[:2]

    for xx in range(row):
        for yy in range(column):
            XY1 = np.array([xx,yy,1])
            new_XY = np.array(A @ XY1)
            new_XY = np.round(new_XY / new_XY[2]).astype(np.int)
            
            if check_out_of_bound(row, column, new_XY):
                continue
                
            try:
                #res[xx,yy] = img[new_XY[0], new_XY[1]]
                res[new_XY[0], new_XY[1]] = img[xx,yy]
            except IndexError:
                continue
    return res

def rotation(img, angle):
    H = get_rotation(angle)
    
    res = transform(img, H)
    return res

def get_rotation(angle):
    angle = np.radians(angle)
    return np.array([
        [np.cos(angle), np.sin(angle), 0],
        [-np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])

def check_out_of_bound(h, w, xy):
    if (xy[0] > w-1 or xy[0] < 0):
        return True
    if (xy[1] > h-1 or xy[1] < 0):
        return True
    return False

row, column = img.shape[:2]

res = rotation(img, 30)

_, axarr = plt.subplots(1,2)
axarr[0].imshow(img.astype('uint8'))
axarr[1].imshow(res.astype('uint8'))
plt.show()