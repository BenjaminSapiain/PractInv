# Importaciones necesarias
import json
import os
image_path = '/Darknet/data'

# Creaci ón de archivo classes . txt
with open(image_path +  'Dataset/annotation_definitions.json', 'r') as file:
    classes_json_file = json.load(file)

with open(image_path + "RGB/classes.txt" , 'w') as classes_file:
    for classe in classes_json_file['annotation_definitions'][0]['spec']:
        classes_file.write(
        '%s\n'%(
            classe ['label_name']    
        )
    )

# Crear anotaciones . txt en formato YOLO para cada imagen
pic_height = 640
pic_width = 640

dir_list = os. listdir(image_path + 'Dataset/')

captures_list = [str for str in dir_list if any (sub in str for sub in ["captures"])]

for capture in captures_list :
    with open(image_path + 'Dataset/' + capture , 'r') as file :
        big_json_file = json . load ( file )
    for picture in big_json_file ['captures']:
        filename = picture ['filename']. split ('/') [ -1]
        filename = filename [: -4] + '.txt '
        with open ( image_path + 'RGB/' + filename , 'w') as annotation_file:
            for bbox in picture ['annotations'][0]['values']:
                annotation_file.write(
                    '%d %f %f %f %f\n' % (
                        bbox['label_id'],
                            (bbox['x'] + bbox ['width']/2) / pic_width ,
                            (bbox['y'] + bbox ['height']/2) / pic_height ,
                            bbox ['width'] / pic_width ,
                            bbox ['height'] / pic_height
                    )
                )

