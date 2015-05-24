from scipy import misc
from glob import glob
file_names = glob('*.png')
for file_name in file_names:
    image = misc.imread(file_name)
    arr = image.reshape(4096)/255.0
    with open('output.txt','a') as out:
        for itm in arr:
            out.write(str(itm) + ',')
        out.write('\n')
