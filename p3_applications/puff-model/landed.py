#Code from http://publish.illinois.edu/pillsburydoughcat/puff-model/puff-model-supplementary-material/
#landed
import numpy as np
from parameters import *
 
def landed(H,A):
    for i in xrange(0,num_particles):
        if A[i] == 1.0 and H[i] <= 0.0:
            A[i] = 0.0
            H[i] = 0.0
        if H[i] > alt_coor[29]:
            H[i] = alt_coor[29]
        if H[i] <= 0.0:
            H[i] = 0.0
    return A, H
