from PIL import Image
from datetime import datetime

def getDate(image_path):
    image = Image.open(image_path)
    return image.getexif().get(306)

def matchesDate(date_string):
    date = datetime.strptime(date_string, "%Y:%m:%d %H:%M:%S")
    year = 2006
    month = 9

    if date.month == month and date.year == year:
        return True
    return False


def openImage(image_path):
    image = Image.open(image_path)
    image.show()

