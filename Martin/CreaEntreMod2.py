import pandas as pd
from sklearn.model_selection import train_test_split
import joblib

dataset = pd.read_csv('USADO_dataset_m2.csv')

for x in range(dataset['Forma'].shape[0]):
  if dataset['Forma'][x] == 'Bacilo':
    dataset['Forma'][x] = 0
  elif dataset['Forma'][x] == 'Coccus':
    dataset['Forma'][x] = 1
  elif dataset['Forma'][x] == 'CoccusBacilos':
    dataset['Forma'][x] = 2
  elif dataset['Forma'][x] == 'Spirillum':
    dataset['Forma'][x] = 3

for x in range(dataset['Estado'].shape[0]):
  if dataset['Estado'][x] == 'conocido':
    dataset['Estado'][x] = 0
  elif dataset['Estado'][x] == 'desconocido':
    dataset['Estado'][x] = 1

X = dataset[['LargoUm','AnchoUm','Forma']]
# print(X)

Y = dataset [['Estado']]
Y = Y.astype('int')
# print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.10)

# Support Vector Machines (SVM)
from sklearn.svm import SVC
# Entrenamiento
svc = SVC(kernel = "linear")
#Se trabaja con el input pero en data numerica.
svc.fit(X_train.values, Y_train.values.ravel())

# Almacenar SVM


joblib.dump(svc, 'SVM_joblib_infra2')