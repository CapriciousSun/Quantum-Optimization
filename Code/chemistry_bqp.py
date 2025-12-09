from bqphy import BQPhy_Optimiser
import numpy as np

def atomic_fitness(element : int):
  """
  Fitness function of an atom - used for atomic ground state (electronic) energy estimation.
  The global minimum corresponds to the lowest possible energy state that the atom can be in.

  Args:
    element: An integer that represents the atomic number of the element

  Returns:
    Array of float: The positions of the electrons

  """

  # --- Objective --- 
  
  fitness = []


  for i in range(element):
		phi = parts * i
		terms['e' + str(i + 1)] = []
		terms['e' + str(i + 1)].append(np.cos(phi))
		terms['e' + str(i + 1)].append(np.sin(phi))

  # -- Constraints ---

  
  return fitness

def main():
  config = {
    "numPopulation": 50,
    "maxGeneration": 100,
    "deltaTheta": 0.05,
    "designVariables": 2,
    "typeOfOptimisation": "CONTINUOUS",
    "lowerBounds": [-10.0] * 6,
    "upperBounds": [10.0] * 6,
  }