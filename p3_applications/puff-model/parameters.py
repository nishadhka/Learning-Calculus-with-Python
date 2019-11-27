#Code from http://publish.illinois.edu/pillsburydoughcat/puff-model/puff-model-supplementary-material/
import numpy as np
#parameters
 
num_particles = 1000
time = 5.0 #days
dt = 10.0 * 60.#minutes
time_steps = int(time * 24.0 * 3600. / dt) + 1
 
D_log = np.zeros((num_particles))
for i in xrange(0,num_particles):
    D_log[i] = np.random.normal(-5.0,2.5)
D = 10. ** (D_log)
 
K_h = 2.0 * (10. **4.)
K_v = 10.
 
start_lat = 15.141667
start_lon = 120.35
 
sigma_lon = .01
sigma_lat = .01
 
U = np.load('u_wind.npy')
V = np.load('v_wind.npy')
W = np.load('w_wind.npy')
 
alt_coor = np.linspace(0,29000,30)
lat_coor = np.linspace(-90.,90.,73)
lon_coor = np.linspace(0.,360.,144)
