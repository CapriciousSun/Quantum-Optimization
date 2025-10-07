20250930182319

Tags:

## Formalism
It is an evolutionary process where variables are mapped to binary qubits and then evolved using quantum gates. It is better than certain techniques like genetic algorithms in finding the global optima of a system. It works with *"populations"* of values, where each population is evaluated for its *"fitness"* based on arbitrary constraints. 

## Process
The process of QIO is as following
1. Initialization with Hadamard gates
2. Applying rotation gates with Pauli rotation gates
3. Measurement
4. Evaluation for fitness
5. Finding the best population and updating the rotation values
6. Applying rotation gates with the updated values
7. Repeat steps 3 to 6

## Benchmarking
Benchmarking are done with a variety of functions, like the Ackley function. 

## Use Cases
- Drone swarm movement
- Material design
- Airport gate operations
- Satellite scheduling
Speed up is given from data complexity, not something like Shor's algorithm, where it's a computing space complexity. 

## Comparison to Genetic Algorithms
Genetic algorithms require cross over, the mix and matching of "genetic" information whereas QIO only requires the updating of rotation information.

## Speedup
QIO's Hilbert space increases linearly whereas classical methods increase logarithmically. 
___
# References

