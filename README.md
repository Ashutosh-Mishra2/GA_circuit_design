# Quantum Circuit design using Genetic Algorithm
![image](https://user-images.githubusercontent.com/61776089/221840127-68fd5b97-f140-498f-94c9-9a2feed8880a.png)


## Team quantum_cats
Members: Ashutosh Mishra, Taradutt Pattnaik, Shivnag Sista

## Project description
### Motivation

Several applications in quantum computing, quantum information and quantum communication require the preparation of entangled quantum states such as the Bell state, the W state or the GHZ (Greenberger-Horne-Zeilinger) state. One can prepare these states by starting with some initial quantum state and applying **quantum gates** on this state until the target state is reached. This sequence of quantum gates that transform a given initial state to some final state is referred to as a quantum circuit.

Constructing quantum circuits which prepare the required state is often a non-trivial task. Traditionally, the circuits were designed by hand, using a combination of trial and error and accumulated experience to identify design patterns and reusable units from previously made circuits. This process is often tedious very hard to do for all but the simplest of circuits. Furthermore, such a manually constructed circuit is not guaranteed to be the most efficient circuit (i.e. of the lowest circuit depth) which achieves the task.

This is where classical optimization algorithms enter the picture. One may use these algorithms to search the space of possible circuits (subject to some constraints) and identify the circuit which most efficiently produces the required quantum state. There are several approaches to performing such optimization. Of these, the approach we used in this project is **genetic algorithms**.


### Codes
The codes can be found in the Jupyter notebook `quantum_circuit_design.ipynb`. Also some other functions are defined in the file `helper_function.py`.


### Dependecies and installation
We use [pennylane](https://pennylane.ai/) to simulate the quantum circuits. The installation instructions can be found [here](https://pennylane.ai/install.html). 
