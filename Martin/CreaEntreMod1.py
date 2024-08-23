import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib

dataset = pd.read_csv('USADO_dataset_m1.csv')

for x in range(dataset['Forma'].shape[0]):
  if dataset['Forma'][x] == 'Bacilo':
    dataset['Forma'][x] = 0
  else: #dataset['Forma'][x] == 'Coccus':
    dataset['Forma'][x] = 1

for x in range(dataset['Tipo'].shape[0]):
  if dataset['Tipo'][x] == 'ecoli':
    dataset['Tipo'][x] = 0
  elif dataset['Tipo'][x] == 'scerevisiae':
    dataset['Tipo'][x] = 1

X = dataset[['LargoUm','AnchoUm']]
Y = dataset[['Tipo']]
Y = Y.astype('int')

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.20)

# Support Vector Machines (SVM)
# from sklearn.svm import SVC
# #Entrenamiento
# svc = SVC(kernel = " linear")
# #Se trabaja con el input pero en data numerica.
# svc.fit(X_train, Y_train.values.ravel())
# print(svc.predict([[8.546, 8.546]]))

# Arboles de decision
# from sklearn.tree import DecisionTreeClassifier
# dec_tree = DecisionTreeClassifier()
# dec_tree.fit(X_train,Y_train.values.ravel())
# print(dec_tree.predict([[8.546, 8.546]]))

# Naive Bayes
# from sklearn.naive_bayes import GaussianNB
# naiveB = GaussianNB()
# naiveB.fit(X_train,Y_train.values.ravel()) #Es necesario pasarlo a array
# print(naiveB.predict([[8.546, 8.546]]))

#KNN (Algoritmo escogido)

knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train.values,Y_train.values.ravel())

# Prueba de predicción
# print(knn.predict([[8.546, 8.546]]))

# Almacenar KNN
joblib.dump(knn,'knn_joblib_infra')
print("Modelo almacenado")
