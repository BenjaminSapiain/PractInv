import json

def lectura():
    with open('result.json') as f:
        payload = json.load(f)

        largo = []
        ancho = []
        forma = []
        organismo = []

        for microor in payload:
            if microor['image_id'] == 1:
                largoAux = abs(microor['bbox'][0] - microor['bbox'][1])
                anchoAux = abs(microor['bbox'][2] - microor['bbox'][3])
                largo.append(largoAux/500)
                ancho.append(anchoAux/500)
            elif microor['image_id'] == 4:
                largoAux = abs(microor['bbox'][0] - microor['bbox'][1])
                anchoAux = abs(microor['bbox'][2] - microor['bbox'][3])
                largo.append(largoAux/140)
                ancho.append(anchoAux/140)
            else:
                largoAux = abs(microor['bbox'][0] - microor['bbox'][1])
                anchoAux = abs(microor['bbox'][2] - microor['bbox'][3])
                largo.append(largoAux/100)
                ancho.append(anchoAux/100)
            if microor['category_name'] == 'rod':
                forma.append('Bacilos')
            elif microor['category_name'] == 'spiral':
                forma.append('Spirillum')
            elif microor['category_name'] == 'sphere':
                forma.append('Coccus')
        organismo.append(largo)
        organismo.append(ancho)
        organismo.append(forma)
    return organismo

        
