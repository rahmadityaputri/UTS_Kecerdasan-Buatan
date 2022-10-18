import numpy as np

inputs = [12.0, 11.5, 2.1, 2.5, 2.0, 1.1, 2.9, 11.5, 12.0, 1.5]
weights = [
    [11.2, 2.4, 1.6, 2.8, 1.0, 0.2, 1.4, 0.6, 1.8, 10.0],
    [10.7, 4.8, 0.6, 22.8, 0.6, 2.6, 10.6, 2.8, 10.6, 12.1],
    [13.7, 1.1, 3.6, 11.8, 3.6, 1.0, 1.6, 1.3, 3.1, 1.0],
    [2.1, 1.5, 2.6, 1.4, 2.6, 16.8, 2.5, 1.8, 12.0, 11.8],
    [1.5, 2.8, 0.6, 3.8, 0.6, 1.8, 1.6, 17.8, 2.6, 11.1],
]

biases = [13.5, 2.2, 9.0, 1.2, 1.0]

outputs = np.dot(weights, inputs) + biases
print(outputs)