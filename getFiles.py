from os import listdir
from os.path import isfile, join

mypath='C:\\Users\\IgorDC\Documents\\AutoFormFillerFiles'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)



