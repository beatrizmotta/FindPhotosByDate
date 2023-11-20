import os
import re 
from DateImageHelper import getDate, openImage, matchesDate

file_extensions = "jpg|png|jpeg"

def getFileType(fileName):
    file = fileName.split(".")
    extension = file[1]
    return extension

def checkFileType(fileType):
    return re.search(file_extensions, fileType, re.IGNORECASE)

for root, dirs, files in os.walk(".", topdown=True):
    for name in files:
        path = os.path.join(root, name)

        if (checkFileType(path)):
            date = getDate(path)
            print(date, path)

            if date != None and matchesDate(date):
                openImage(path)
                continue
        


        
