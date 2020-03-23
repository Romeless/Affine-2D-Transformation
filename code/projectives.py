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

def projective(img, original_4_points=None, final_4_points=None):
    row, column = img.shape[:2]
    
    try:
        if original_4_points == None:
            original_4_points = np.array([
                [0,0],[column-1,0],
                [0,row-1],[column-1,row-1]
            ])
        
        if final_4_points == None:
            final_4_points = np.array([
                [0,0],[column-1,np.int(row / 4)],
                [0,row-1],[column-1,np.int(row * 3 / 4)]
            ])
    except:
        pass
        
    H = search_4_variables(original_4_points, final_4_points)
    res = transform(img, H)
    return res

def search_4_variables(ori, fin):
    #https://math.stackexchange.com/questions/494238/how-to-compute-homography-matrix-h-from-corresponding-points-2d-2d-planar-homog
    P = np.empty([1,9])
    for i in range(ori.shape[0]):
        x = ori[i][0]
        y = ori[i][1]
        xx = fin[i][0]
        yy = fin[i][1]
        top = np.array([[-x,-y,-1, 0, 0, 0,x * xx,y * xx, xx]])
        bot = np.array([[ 0, 0, 0,-x,-y,-1,x * yy,y * yy, yy]])
        P = np.append(P, top, axis=0)
        P = np.append(P, bot, axis=0)
    P = np.append(P, np.array([[0,0,0,0,0,0,0,0,1]]), axis=0)
    P = P[1:,:]
    
    #inverse P
    invP = np.linalg.inv(P)
    ans = np.zeros([9,1])
    ans[8,0] = 1
    
    H = invP @ ans
    return H.reshape((3,3))
    
def check_out_of_bound(h, w, xy):
    if (xy[0] > w-1 or xy[0] < 0):
        return True
    if (xy[1] > h-1 or xy[1] < 0):
        return True
    return False

row, column = img.shape[:2]

ori = np.array([
    [0,0],[column-1,0],
    [0,row-1],[column-1,row-1]
])
        
fin = np.array([
    [0,0],[column-1,0],
    [np.int(column / 4),row-1],[np.int(column * 3/4),row-1]
])

res = projective(img, ori, fin)

_, axarr = plt.subplots(1,2)
axarr[0].imshow(img.astype('uint8'))
axarr[1].imshow(res.astype('uint8'))
plt.show()