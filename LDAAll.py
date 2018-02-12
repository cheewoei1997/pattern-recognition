import numpy as np
import matplotlib.pyplot as plt

# Load training and testing data
X_train = np.loadtxt('TrainAll.txt')
y_train = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3])
X_test = np.loadtxt('TestAll.txt')

print("Shape of training set: {}".format(X_train.shape))
print("Shape of training label: {}".format(y_train.shape))
print("Shape of testing set: {}".format(X_test.shape))

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 
lda = LinearDiscriminantAnalysis(n_components=5)

lda.fit(X_train, y_train)
X_train_lda = lda.transform(X_train)
X_test_lda = lda.transform(X_test)

print("Shape of training set: {}".format(X_train_lda.shape))
print("Shape of testing set: {}".format(X_test_lda.shape))

# Calculate distances

intra_class_dist = np.sum(np.power((X_train_lda[1,:] - X_test_lda[1,:]),2))
inter_class_dist = np.sum(np.power((X_train_lda[1,:] - X_test_lda[6,:]),2))
print("Intra-class distance: %d" % (intra_class_dist))
print("Inter-class distance: %d" % (inter_class_dist))

