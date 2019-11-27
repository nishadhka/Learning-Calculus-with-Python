#Code from http://publish.illinois.edu/pillsburydoughcat/puff-model/puff-model-supplementary-material/
import numpy as np
from parameters import *
R = np.zeros((num_particles,3))
 
def initial(sigma_lat,sigma_lon):
    for i in xrange(0,num_particles):
        R[i,0] = 15000.* np.random.uniform()
        R[i,1] = np.random.normal(start_lat,sigma_lat)
        R[i,2] = np.random.normal(start_lon,sigma_lon)
 
    return R
