#Code from http://publish.illinois.edu/pillsburydoughcat/puff-model/puff-model-supplementary-material/
import numpy as np
from parameters import *
R_advection = np.zeros((num_particles))

def advectiony(R,A,T,t):
for i in xrange(0,num_particles):
if A[i] == 1 and R[i,0] > 0.0:
alt_part = R[i,0]
lat_part = R[i,1]
lon_part = R[i,2]
a = int(R[i,0]/29000.*29.)
b = int((R[i,1]+90.)/180.*73.)
c = int(R[i,2]/360.*144.)
if a == 29:
a_high = a
else:
a_high = a+1

alt_low = alt_coor[a]
alt_high = alt_coor[a_high]
lat_down = lat_coor[b]
lat_up = lat_coor[b+1]
lon_left = lon_coor
lon_right = lon_coor

#time 1
interp_x1 = (lon_part – lon_left) / (lon_right – lon_left) * (V[T,a,b,c+1] – V[T,a,b,c]) + V[T,a,b,c]
interp_x2 = (lon_part – lon_left) / (lon_right – lon_left) * (V[T,a,b+1,c+1] – V[T,a,b+1,c]) + V[T,a,b+1,c]
interp_x3 = (lon_part – lon_left) / (lon_right – lon_left) * (V[T,a_high,b,c+1] – V[T,a_high,b,c]) + V[T,a_high,b,c]
interp_x4 = (lon_part – lon_left) / (lon_right – lon_left) * (V[T,a_high,b+1,c+1] – V[T,a_high,b+1,c]) + V[T,a_high,b+1,c]

interp_y1 = (lat_part – lat_down) / (lat_up – lat_down) * (interp_x2 – interp_x1) + interp_x1
interp_y2 = (lat_part – lat_down) / (lat_up – lat_down) * (interp_x4 – interp_x3) + interp_x3

if a_high == a:
V_interp_1 = (interp_y1+interp_y2)/2.0
else:
V_interp_1 = (alt_part – alt_low) / (alt_high – alt_low) * (interp_y2 – interp_y1) + interp_y1

#time 2
interp_x1 = (lon_part – lon_left) / (lon_right – lon_left) * (V[T+1,a,b,c+1] – V[T+1,a,b,c]) + V[T+1,a,b,c]
interp_x2 = (lon_part – lon_left) / (lon_right – lon_left) * (V[T+1,a,b+1,c+1] – V[T+1,a,b+1,c]) + V[T+1,a,b+1,c]
interp_x3 = (lon_part – lon_left) / (lon_right – lon_left) * (V[T+1,a_high,b,c+1] – V[T+1,a_high,b,c]) + V[T+1,a_high,b,c]
interp_x4 = (lon_part – lon_left) / (lon_right – lon_left) * (V[T+1,a_high,b+1,c+1] – V[T+1,a_high,b+1,c]) + V[T+1,a_high,b+1,c]

interp_y1 = (lat_part – lat_down) / (lat_up – lat_down) * (interp_x2 – interp_x1) + interp_x1
interp_y2 = (lat_part – lat_down) / (lat_up – lat_down) * (interp_x4 – interp_x3) + interp_x3

if a_high == a:
V_interp_2 = (interp_y1+interp_y2)/2.0
else:
V_interp_2 = (alt_part – alt_low) / (alt_high – alt_low) * (interp_y2 – interp_y1) + interp_y1

R_advection[i] = (V_interp_2 – V_interp_1) / 1.0 * (t – float(T)) + V_interp_1

else:
R_advection[i] = 0.0

return R_advection
