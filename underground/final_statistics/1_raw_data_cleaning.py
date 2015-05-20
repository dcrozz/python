##change the station id
dct = {'268019':260032,'268004':'260036','268009':'261005','268021':'261007','263032':'261018','263024':'262016'}
from glob import glob
from time import time
file_names = glob('[0-9]'*8 + '.txt')
for file_name in file_names:
    starttime = time()
    lst = []
    with open(file_name) as data:
        lines = data.readlines()
        for line in lines:
            cur_line = line.strip().split('\t')
            if dct.get(cur_line[1]):
                cur_line[1] = str(dct.get(cur_line[1]))
            if dct.get(cur_line[2]):
                cur_line[2] = str(dct.get(cur_line[2]))
            lst.append(cur_line)
    with open(file_name[:-4] + 'c.txt','w') as out:
        for item in lst:
            out.write(','.join(item) + '\n')
    endtime = time()
    print file_name + ' ' + str(endtime-starttime)
