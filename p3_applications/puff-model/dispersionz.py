#Code from http://publish.illinois.edu/pillsburydoughcat/puff-model/puff-model-supplementary-material/
#dispersion
import numpy as np
from parameters import *
R_dispersion = np.zeros((num_particles))
 
def dispersionz(A):
    c_v = np.sqrt(2.0 * K_v /dt)
    for i in range(0,num_particles):
        if A[i] == 1:
            R_dispersion[i] = np.random.normal(0.0,c_v)
        else:
            R_dispersion[i] = 0.0
 
    return R_dispersion
