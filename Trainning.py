from PyWANN import WiSARD as wi
import numpy as np
import Reader as r

# OBS: data eh matriz e labels eh vertor
data, labels = r.get_data_and_labels()

# percorrer data e labels treinando, para cada classe, cada retina
# data_teste = [[0, 0, 0], [1, 0, 0], [1, 1, 1]]
# labels_teste = ["class_a", "class_b", "class_c"]

retina_length = 784
num_bits_addr = 2
bleaching = True

w = wi.WiSARD(num_bits_addr, bleaching)

# training discriminators
print("fit")
w.fit(data, labels)

print("predict")
array = np.zeros((1,784))
print (array)
result = w.predict(array)
print (result)