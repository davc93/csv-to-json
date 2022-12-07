import os
import json
import pandas as pd

def csvTojson():
    filename = input('Ingresa el nombre del archivo => ')
    filepath = os.path.join('inputs',filename)

    outputPath = os.path.join('outputs',f'{filename.split(sep=".")[0]}.json') 
    with open(outputPath,'w') as readedFile:
        readedFile.write("")
        readedFile.close()

    outputData = pd.DataFrame(pd.read_csv(filepath,sep=",",header=0))
    outputData.to_json(outputPath,orient='records',date_format="epoch",double_precision=10,force_ascii=True)

def csvTojsonArrays():
    filename = input('Ingresa el nombre del archivo => ')
    filepath = os.path.join('inputs',filename)
    outputPath = os.path.join('outputs',f'{filename.split(sep=".")[0]}.json') 
    data = pd.DataFrame(pd.read_csv(filepath,sep=",",header=0)).to_json(orient='records')
    jsonFile = json.loads(data)
    for i in jsonFile:
        i['videos'] = i['videos'].split(";")
        i["images[Solo si estan las imagenes subidas a lagun otro lugar]"] = i["images[Solo si estan las imagenes subidas a lagun otro lugar]"].split(";")
    print(jsonFile)
    print(outputPath)
    with open(outputPath,'w') as readedFile:
        readedFile.write(json.dumps(jsonFile))
        readedFile.close()
    



csvTojsonArrays()


