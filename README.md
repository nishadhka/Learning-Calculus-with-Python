# Learning-Calculus-with-Python

Python with easy to read and learn features is an wonderful learning aid. It sets up perfect tool to know about calculus and its real-world applications. This workshop goes through the use of calculus in three simulation examples and aims to give a basic introduction and learning pathways for numerical modeling.  The first example is about taxi trip simulation, second on trajectory models and third on simulation using Pyclaw library. We will have introductory exercise on basic of calculus, different concepts involved in the cases.  

**Workshop outline**

1. Introduction to calculus with Python (50 minutes)
*  Calculus basics, [Notebook](https://github.com/nishadhka/Learning-Calculus-with-Python/blob/master/introduction/Calculus-Differentiation-Integration.ipynb)
        * Derivatives
        * Integrals
        * Limits
        * Series expansion
        * Finite differences
        * Solving deferential equations
        * Integration of simple function
* Some interesting Numerical simulations 
        * Population-Growth-model, [Notebook](https://github.com/nishadhka/Learning-Calculus-with-Python/blob/master/introduction/Population-Growth-model.ipynb)
        * Prey-Predator-Model, [notebook](https://github.com/nishadhka/Learning-Calculus-with-Python/blob/master/introduction/Prey-Predator-Model.ipynb)
        * Climate-model, [notebook](https://github.com/nishadhka/Learning-Calculus-with-Python/blob/master/introduction/Climate-model.ipynb)
        * Brownian-motions-simulation, [notebook](https://github.com/nishadhka/Learning-Calculus-with-Python/blob/master/introduction/Brownian-motions-simulation.ipynb)
        * Extras: 1D-Wave equation simulation
        * Extras: Large Eddy Simulation of Ocean (in Julia)
 
2. Exercises
* **Taxi trip simulation (15 minutes):**
Taxi trip data gives orgin, destination and duration details of a trip. The real world movement of the taxi will be simulated. Uber taxi trip and Open Street Map data will be used, Bangalore city is simulation domain.       
* **Trajectory models (15 minutes):**
PUFF model is a Lagrangian particle model which simulate trajectory of particles emitted from volcanic eruptions. Using a case study data on volcanic eruption, the model will be simulated.
* **Pyclaw library (30 minutes):**
Pyclaw is a python based solver for partial differential equations. This library is being used for various geophysical simulations, a demonstration on its example.


**Prerequisites**

Python 3 with Numpy, Scipy, SymPy and Matplotlib is prerequisite for examples 1 and 2, Pyclaw is required for example3


**Workshop content**

Workshop example contents are based on 

1. Jeffrey's and his cat's website, http://publish.illinois.edu/pillsburydoughcat/
2. Svein Linge and Hans Petter Langtangen (2016) Programming for Computations - A Gentle Introduction to Numerical Simulations with Python, https://hplgit.github.io/prog4comp/doc/pub/p4c_Python.pdf
