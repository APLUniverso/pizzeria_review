from json import dump, load

def readFile(fileName): # Lee el archivo
    try:
        fileData = None
        with open(fileName) as f:
            fileData = load(f)
        return fileData
    except FileNotFoundError: # Si no existe lo crea vacio
        saveFile(fileName,{})
        return readFile(fileName)

def saveFile(fileName,data): # Guarda la informacion del archivo
    with open(fileName,"w") as f:
        dump(data,f,indent=4)