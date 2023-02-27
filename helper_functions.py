import pennylane as qml
import pennylane.numpy as np
import matplotlib.pyplot as plt




def inner_product(state1, state2):
    """
    Calculate the inner product of two input state vectors.

    Args:
        state1 (np.ndarray): State 1
        state2 (np.ndarray): State 2

    Returns:
        np.complex: Inner product of State1 and State2
    """
    return np.abs(np.matmul(
        np.conjugate(np.transpose(state1)), 
        state2
    ))**2


def qml_to_qasm(circuit):
    """
    Print the input circuit in QASM format.

    Args:
        circuit (List[qml.operation.Operation]): Input circuit as a list of operators.
    """
    for i in range(len(circuit)):
        if circuit[i].name == "CNOT":
            print(f"cx q[{circuit[i].wires[0]}], q[{circuit[i].wires[1]}];")
        elif circuit[i].name == "RX":
            print(f"rx({np.round(circuit[i].parameters[0],2)}) q[{circuit[i].wires[0]}];")
        elif circuit[i].name == "RY":
            print(f"ry({np.round(circuit[i].parameters[0],2)}) q[{circuit[i].wires[0]}];")
        elif circuit[i].name == "RZ":
            print(f"rz({np.round(circuit[i].parameters[0],2)}) q[{circuit[i].wires[0]}];")
