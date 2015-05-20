def read_usr():
    usr_dct = {}
    file_name = open('All_User.txt')
    lines = file_name.readlines()
    for line in lines:
        cur_line = line.strip().split(',')
        usr_dct[cur_line[0]] = 1
    return usr_dct

if __name__ == "__main__":
    from glob import glob
    from time import time
    usr_dct = {} 
    usr_dct = read_usr()
    file_names = glob('[0-9]'*8 + '.txt')
    for file_name in file_names:
        starttime = time()
        with open(file_name) as data:
            lines = data.readlines()
            for line in lines:
                cur_line = line.strip().split(',')
                if usr_dct.get(cur_line[0],0) == 1 :
                    cur_line.append(file_name[0:8])
                    with open(cur_line[0] + '.txt','a') as out:
                        out.write(','.join(cur_line) + '\n')
        endtime = time()
        print file_name +' '+ str(endtime-starttime)
