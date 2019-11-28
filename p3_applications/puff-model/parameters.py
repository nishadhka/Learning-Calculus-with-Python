#Code from http://publish.illinois.edu/pillsburydoughcat/puff-model/puff-model-supplementary-material/
import numpy as np
#parameters
 
num_particles = 1000
time = 5.0 #days
dt = 10.0 * 60.#minutes
time_steps = int(time * 24.0 * 3600. / dt) + 1
 
D_log = np.zeros((num_particles))
for i in range(0,num_particles):
    D_log[i] = np.random.normal(-5.0,2.5)

#diameter of the particle
D = 10. ** (D_log)

# horizontal dispersion coefficient 
K_h = 2.0 * (10. **4.)
# vertical dispersion coefficient
K_v = 10.

#initial location of the particles, i.e. the volcano location 
start_lat = 15.141667
start_lon = 120.35

#the spread of the initial plume, in decimal degrees. 
sigma_lon = .01
sigma_lat = .01

#meterological paramters 
U = np.load('u_wind.npy')
V = np.load('v_wind.npy')
W = np.load('w_wind.npy')
 


alt_coor = np.linspace(0,40000,41)
lat_coor = np.linspace(3,40,161)
lon_coor = np.linspace(64.,101.,161)
