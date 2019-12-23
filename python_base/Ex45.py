from PIL import Image

fileName = "./Ex45_file/tuxiang.jpg"
img = Image.open(fileName)

imgSize = img.size

print(imgSize)
