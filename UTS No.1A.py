import numpy as np

inputs = [13.0, 15.5, 11.1, 2.1, 4.1, 13.5, 1.9, 12.5, 3.4, 4.1]
weights = [14.2, 2.6, 1.3, 31.8, 42.0, 10.2, 11.4, 2.7, 1.4, 12.0]

bias = 5.6

outputs = np.dot(weights, inputs) + bias
print(outputs)