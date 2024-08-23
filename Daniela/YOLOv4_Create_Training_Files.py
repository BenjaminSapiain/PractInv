# Importaciones necesarias
import os

# Direcci ón de la carpeta generada por Unity
image_path = '/Darknet/data/RGB'
os.chdir(image_path)

# Iteraci ón por cada imagen del directorio y guardado de la dirección de cada imagen en el arreglo path_list
path_list = []
for current_dir, dirs, files in os.walk ('.'):
    for f in files :
        if f.endswith('.jpg'):
            file_loc = image_path + '/' + f
            path_list.append(file_loc + '\n')

# División de los datos en un ratio de 80:20
# Se obtienen 20 % de los datos y se guardan en el archivo de testeo
path_list_test = path_list[:int(len(path_list) * 0.20)]

# Se eliminan 20 % de los datos seleccionados como testeo, quedan 80% de datos para entrenamiento
path_list = path_list[int(len(path_list) * 0.20):]

# Creación de archivo train.txt y escritura del 80 % de los datos
with open('train.txt', 'w') as train:
    for i in path_list:
        train.write(i)

# Creaci ón de archivo test .txt y escritura del 20 % de los datos
with open('test.txt', 'w') as test:
    for i in path_list_test:
        test.write(i)

# Inicializaci ón de contador
i = 0

# Crear archivo classes.names desde el contenido existente de classes.txt
with open(image_path + '/' + 'classes.names', 'w') as cls, \
     open(image_path + '/' + 'classes.txt' , 'r') as text:
    for l in text:
        cls.write(l)
        i += 1

# Creación de archivo image_data.data
with open(image_path + '/' + 'image_data.data', 'w') as data :
    # Escritura del nú mero de clases
    data.write('classes = ' + str (i) + '\n')

    # Escritura de la direcci ón del archivo train . txt
    data.write('train = ' + image_path + '/' + 'train.txt' + '\ n')

    # Escritura de la direcci ón del archivo test . txt
    data.write('valid = ' + image_path + '/' + 'test.txt' + '\n')

    # Escritura de la direcci ón del archivo classes . names
    data.write('names = ' + image_path + '/' + 'classes.names' + '\n')

    # Espicificaci ón de la dirección de la carpeta donde se guardarán los pesos entrenados del modelo
    data.write('backup = backup')
