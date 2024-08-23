# Importaciones necesarias
import json
import os

# Dirección hacia la carpeta Dataset generada por Unity
dataset_path = '/result/'

# Direcci ón hacia la carpeta de destino
dataset_path_final = '/result/files/'

# Creaci ón de la carpeta para las anotaciones
import os.path
from os import path

if path.exists(dataset_path_final) == False:
    os.mkdir(dataset_path_final)

    os.mkdir(dataset_path_final + 'labels')
    os.mkdir(dataset_path_final + 'labels/train')
    os.mkdir(dataset_path_final + 'labels/val')
    os.mkdir(dataset_path_final + 'labels/test')

    os.mkdir(dataset_path_final + 'images')
    os.mkdir(dataset_path_final + 'images/train')
    os.mkdir(dataset_path_final + 'images/val')
    os.mkdir(dataset_path_final + 'images/test')

# Creaci ón de anotaciones.txt y estructuraci ón en formato YOLOv5 para cada imagen
pic_height = 640
pic_width = 640

dir_list = os.listdir(dataset_path + 'Dataset/')
captures_list = [str for str in dir_list if any (sub in str for sub in ["captures"])]

total_images = len(os.listdir(dataset_path + 'RGB/'))
i = 0
ratio_val = 0.2

for capture in captures_list:
    with open(dataset_path + 'Dataset/' + capture , 'r') as file:
        big_json_file = json.load(file)
    for picture in big_json_file ['captures']:
        filename = picture['filename'].split('/') [ -1]
        filename = filename[:-4]
        i = i + 1
        if(i <= total_images * ratio_val):
            sub_path = "val/"
        else:
            sub_path = "train/"
        with open(dataset_path_final + 'labels/' + sub_path + filename + '.txt', 'w') as annotation_file:
            for bbox in picture ['annotations'][0]['values']:
                annotation_file.write(
                    '%d %f %f %f %f\n' % (
                        bbox['label_id'],
                        (bbox['x'] + bbox['width']/2) / pic_width,
                        (bbox['y'] + bbox['height']/2) / pic_height,
                        bbox['width'] / pic_width,
                        bbox['height'] / pic_height
                    )
                )
        os. rename(dataset_path + 'RGB/' + filename + '.png', dataset_path_final + 'images/'+ sub_path + filename + '.png')
# Creaci ón de archivo . yaml
# Acceso a las classes
with open(dataset_path + 'Dataset/annotation_definitions.json', 'r') as file:
    classes_json_file = json.load(file)

i = 0
classes = ''
for classe in classes_json_file ['annotation_definitions'][0]['spec']:
    classes = classes + "'"+ classe['label_name']+ "',"
    i = i + 1

dir_name = 'train_data'

data_yaml = """
# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]\n
# path: ../""" + dir_name + """ # dataset root dir\n
train: ../""" + dir_name + """/images/train/ # train images (relative to 'path') 128 images\n
val: ../""" + dir_name + """/images/val/ # val images (relative to 'path') 128 images\n
test: # test images (optional)\n
\n
# Classes \n
nc: """ + str(i) + """ # number of classes\n
names: [""" + classes[:-1] + """] # class names\n"""

with open(dataset_path_final + 'data.yaml', 'w') as annotation_file:
    annotation_file.write(data_yaml)
