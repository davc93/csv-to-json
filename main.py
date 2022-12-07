import os
import csv
import json
import pandas as pd

def csvTojson():
    filename = input('Ingresa el nombre del archivo => ')
    filepath = os.path.join('inputs',filename)

    outputName = os.path.join('outputs',f'{filename.split(sep=".")[0]}.json') 
    with open(outputName,'w') as readedFile:
        readedFile.write("")
        readedFile.close()

    outputData = pd.DataFrame(pd.read_csv(filepath,sep=",",header=0))
    print(outputData)
    outputData.to_json(outputName,orient='records',date_format="epoch",double_precision=10,force_ascii=True)
    print(outputData)


csvTojson()


