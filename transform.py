#!/home/romeless/anaconda3/envs/rome/bin/python
# Rama Lesmana
# 1313617011
# University of Jakarta, Indonesia

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

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

def check_out_of_bound(h, w, xy):
    if (xy[0] > w-1 or xy[0] < 0):
        return True
    if (xy[1] > h-1 or xy[1] < 0):
        return True
    return False

def get_scaling(scale_x, scale_y=None):
    try:
        if scale_y == None:
            scale_y = scale_x
    except:
        pass

    return np.array([
        [scale_x, 0, 0],
        [0, scale_y, 0],
        [0, 0, 1]
    ])

def get_translator(x, y):
    return np.array([
        [1, 0, x],
        [0, 1, y],
        [0, 0, 1]
    ])

def get_rotation(angle):
    angle = np.radians(angle)
    return np.array([
        [np.cos(angle), np.sin(angle), 0],
        [-np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])

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

def scaling():
    try:
        H = get_scaling(float(sys.argv[3]))
    except IndexError:
        print("For SCALING: IMAGEPATH SCALE SCALE_X [SCALE_Y]*")
        print("* not mandatory")
        exit()
    return H

def translation():
    try:
        H = get_translator(float(sys.argv[3]), float(sys.argv[4]))
    except IndexError:
        print("For TRANSLATOR: IMAGEPATH TRANSLATE T_X T_Y")
        exit()
    return H

def rotation():
    try:
        H = get_rotation(float(sys.argv[3]))
    except IndexError:
        print("For ROTATE: IMAGEPATH TRANSLATE ANGLE")
        exit()
    return H

def projection():
    try:
        ori, fin = [], []
        for i in range(len(np.array(sys.argv)[3:])):
            if i % 2 == 0:
                ori.append(sys.argv[3+i].split(','))
            else:
                fin.append(sys.argv[3+i].split(','))
        H = search_4_variables(np.array(ori).astype(np.int), np.array(fin).astype(np.int))
    except IndexError:
        print("For PROJECTION: IMAGEPATH PROJECT x1,y1 x'1,y'1 x2,y2 x'2,y'2 x3,y3 x'3,y'3 x4,y4 x'4,y'4 [...]*")
        print("*Can take as many coord as needed, each point must come in pairs of original coord to result coord")
        exit()
    return H

def switch_case(argument):
    switcher = {
        "SCALE": scaling,
        "TRANSLATE": translation,
        "ROTATE": rotation,
        "PROJECT": projection
    }
    func =  switcher.get(argument, lambda:"Invalid argument")
    return func

if __name__ == '__main__':
    import sys
    
    try:
        img = np.array(Image.open(sys.argv[1]))
    except IndexError:
        print("Pass on an imagepath in the arguments")
        exit()
    except:
        print("Invalid imagepath")
        exit()

    try:
        H = switch_case(sys.argv[2])()
    except IndexError:
        print("Pass on command: SCALE / TRANSLATE / ROTATE / PROJECT")
        exit()

    res = transform(img, H)
    res = res.astype("uint8")
    plt.imsave("{}{}{}.jpg".format(sys.argv[1], sys.argv[2], sys.argv[3]), res)
    
    _, axarr = plt.subplots(1,2)
    axarr[0].imshow(img.astype('uint8'))
    axarr[1].imshow(res.astype('uint8'))
    plt.show()
