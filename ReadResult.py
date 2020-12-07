from xml.dom import minidom
import numpy as np
import  matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

mid = open('./ThermalResult/mid.xml', 'w')
with open('./ThermalResult/result.vtu', 'r') as f:
    mid.writelines(f.readlines()[1:])
f.close()
mid.close()

result = minidom.parse('./ThermalResult/mid.xml')

dataArraies = result.getElementsByTagName('DataArray')
for dataArray in dataArraies:
    if dataArray.attributes['Name'].value == 'Temperature:Temperature':
        tmp = dataArray.firstChild.nodeValue
        data = list(map(float, tmp.split()))
        print(f'PointData Num: {len(data)}')
    if dataArray.attributes['Name'].value == 'Points':
        tmp = dataArray.firstChild.nodeValue
        points = list(map(float, tmp.split()))
        print(f'Points Num: {int(len(points)/3)}')
    if dataArray.attributes['Name'].value == 'connectivity':
        tmp = dataArray.firstChild.nodeValue
        connectivity = list(map(int, tmp.split()))
        print(f'connectivity Num: {len(connectivity)}')
    if dataArray.attributes['Name'].value == 'offsets':
        tmp = dataArray.firstChild.nodeValue
        offsets = list(map(int, tmp.split()))
        print(f'offsets Num: {len(offsets)}')
    if dataArray.attributes['Name'].value == 'types':
        tmp = dataArray.firstChild.nodeValue
        types = list(map(int, tmp.split()))
        print(f'types Num: {len(types)}')

# 0 device, 1 heat source, 2 trace
point_type = []
cell_type = []

for d in data:
    if d>41: point_type.append(1)
    else: point_type.append(0)
print('source: ', sum(point_type))

bottom = 3
for index in range(len(point_type)):
    if point_type[index]!=1: continue
    [x,y,z] = points[index*3:index*3+3]
    for ind in range(len(point_type)):
        if point_type[ind]!=0: continue
        [cx,cy,cz] = points[ind*3:ind*3+3]
        if cz<bottom:continue
        if (cx>x-0.1 and cx<x+0.1) or (cy>y-0.1 and cy<y+0.1):
            point_type[ind] = 2

fig = plt.figure()
ax = plt.axes(projection='3d')
px = np.array(points[0::3])
py = np.array(points[1::3])
pz = np.array(points[2::3])
ax.scatter3D(px, py, pz, c=point_type)

max_range = np.array([
    px.max()-px.min(),
    py.max()-py.min(),
    pz.max()-pz.min()]).max()/2.0
mid_x = (px.max()+px.min()) * 0.5
mid_y = (py.max()+py.min()) * 0.5
mid_z = (pz.max()+pz.min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

plt.show()