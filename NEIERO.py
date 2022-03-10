import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

training_inputs = np.array([[0.1969, 0.191, 0.05982],
[0.1958, 0.19055, 0.04348],
[0.19186, 0.1883, 0.05242],
[0.19146, 0.18888, 0.04121],
[0.1921, 0.18725, 0.05557],
[0.1905, 0.1866, 0.03653],
[0.19047, 0.18736, 0.04863],
[0.1899, 0.18582, 0.04689],
[0.18719, 0.1823, 0.06282],
[0.183, 0.17851, 0.06292],
[0.18439, 0.17894, 0.04873],
[0.1825, 0.1771, 0.0592],
[0.18395, 0.178, 0.06652],
[0.18598, 0.18167, 0.06256],
[0.18647, 0.1799, 0.05851],
[0.1904, 0.1835, 0.0763],
[0.19268, 0.19002, 0.06695],
[0.19527, 0.1923, 0.07473],
[0.19339, 0.18578, 0.07266]])

training_outputs = np.array([[0.1918, 0.1893, 0.19083, 0.18786, 0.1904, 0.18976, 0.18598, 0.18276, 0.1815, 0.18285, 0.18129, 0.18201, 0.1823, 0.18644, 0.18985, 0.19221, 0.1927, 0.18659, 0.18231]]).T

np.random.seed(1)

synaptic_weight=2*np.random.random((3,1))-1

print('Случайные инициализирующие веса:')
print(synaptic_weight)

# метод обратного распространения
for i in range(50000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weight))

    err=training_outputs-outputs
    adjustment=np.dot(input_layer.T, err*(outputs*(1-outputs)))

    synaptic_weight+=adjustment

print('Вес после обучения:')
print(synaptic_weight)

print ('Результат после обучения:')
print(outputs)

#ТЕСТ
new_inputs=np.array([0.18514, 0.17842, 0.10335])
output=sigmoid(np.dot(new_inputs, synaptic_weight))

print('новая ситуация')
print(output*1000)
