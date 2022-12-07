import os
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


csvTojson()


