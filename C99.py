import os
import shutil
#os.system("date")
#os.mkdir("C99")
os.getcwd()
print(os.getcwd())
path = '/Users/lokes/Downloads/My Game/sketch.js'
isexist = os.path.exists(path)
print(isexist)
root_ext = os.path.splitext(path)
print("root part ", root_ext[0])
print("extpart ", root_ext[1])
os.listdir()
print(os.listdir())
print("before copying files")
path1 = "/Users/lokes/Downloads/My Game/"
print(os.listdir(path1))
source = "index.html"
destination = "index(copy1).html"
dest = shutil.copy(source, destination)
print("after copying file")
print(os.listdir(path1))
print("before moving file")
print(os.listdir(path1))
source1 = "mp4"
destination1 = "png"
dest1 = shutil.move(source1, destination1)
print("after moving file")
print(os.listdir(path1))