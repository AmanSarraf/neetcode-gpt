import numpy as np
from numpy.typing import NDArray
import math

class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        answer = []
        for n in z:
            sig = 1 / (1 + math.exp(-n))
            answer.append(float(np.round(sig, 5)))
        return answer

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        answer = []
        for n in z:
            answer.append(float(max(0, n)))
        return answer
