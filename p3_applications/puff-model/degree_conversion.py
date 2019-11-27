#Code from http://publish.illinois.edu/pillsburydoughcat/puff-model/puff-model-supplementary-material/
#settling
import numpy as np
from parameters import *
a = 6378137.0
 
def degree_to_dx(R):
    h = R[:,0]
    lat = R[:,1]
    lon = R[:,2]
    dx_lat = np.pi / 180. * (a + h)
    dx_lon = np.pi / 180. * (a + h) * np.cos(lat * np.pi / 180. )
     
    return dx_lat, dx_lon
