import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

x = np.loadtxt('TrainAll.txt')
y = np.loadtxt('TrainLabels.txt')

x_train, x_test, y_train, y_test = train_test_split(x , y)
print(x.shape)
print(y.shape)

scaler = StandardScaler()
scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

mlp = MLPClassifier(hidden_layer_sizes = (93, 93, 93))
mlp.fit(x_train, y_train)
predictions = mlp.predict(x_test)

print(confusion_matrix(y_test, predictions))
print(accuracy_score(y_test, predictions))