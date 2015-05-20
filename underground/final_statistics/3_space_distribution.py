def get_OD_days(column, file_in ):
    data = []
    with open(file_in) as f:
#        with open(file_in[:2]+'-ID_times.txt','w') as out:
        lines = f.readlines()
        for line in lines:
            cur_line = line.strip().split(',')
            data.append( cur_line[0:3] )
    return get_freq_by_index(column,data)  #user frequency
#            out.write(','.join(cur_line)+'\n')

frequency = {}
def get_freq_by_index(k, data):
    freq = {}    
    for itm in data:
        freq[itm[k]] = freq.get(itm[k],0) + 1
    return freq

def add_dict( a, b):
    '''
    add b to a
    a = { 'a':1, 'b':1 }
    b = { 'a':2, 'c':1 }
    a+b = {'a':3, 'b':1, 'c':1} 
    '''
    #assert type(a) == type({}) and type(b) == type({})
    for keyb in b.iterkeys():
        a[keyb] = a.get(keyb,0) + b.get(keyb)
    return a

def sum_of_dict( dct_list ):
    return reduce(add_dict, dct_list)
        

if __name__ == '__main__':
    from glob import glob
    from time import time
    begintime = time()
    file_names = glob('*.txt')
    top1_totallst = []
    top2_totallst = []
    other_totallst = []
    #totalst lst the every top2 [in dict] as a lst
    for file_name in file_names:
        dic_list = []
        starttime =time()
        origin = get_OD_days(1,file_name)
        destination = get_OD_days(2,file_name)
        dic_list.append(origin)
        dic_list.append(destination)
        endtime = time()
        print file_name
        print endtime-starttime
        dct = sum_of_dict(dic_list)
        #sort
        dct_sorted = sorted(dct.items(),key = lambda x:x[1])
        #top1 lst
        top1 = dct_sorted[-1][0]
        top1_tmpdct = {}
        top1_tmpdct[top1] = 1
        top1_totallst.append(top1_tmpdct)
        #top2 lst
        top2 = dct_sorted[-2][0]
        top2_tmpdct = {}
        top2_tmpdct[top2] = 1
        top2_totallst.append(top2_tmpdct)
        #del top1 top2 for otherwise
        del dct[top1]
        del dct[top2]
        for itm in dct.iterkeys():
            dct[itm] = 1
        other_totallst.append(dct)
    with open('top1sum.txt','w') as out:
        top1_sumdct = sum_of_dict(top1_totallst)
        for itm in top1_sumdct.iterkeys():
            out.write(str(itm) +','+ str(top1_sumdct[itm]) + '\n')
    with open('top2sum.txt','w') as out:
        top2_sumdct = sum_of_dict(top2_totallst)
        for itm in top2_sumdct.iterkeys():
            out.write(str(itm) +','+ str(top2_sumdct[itm]) + '\n')
    with open('othersum.txt','w') as out:
        other_sumdct = sum_of_dict(other_totallst)
        for itm in other_sumdct.iterkeys():
            out.write(str(itm) +','+ str(other_sumdct[itm]) + '\n')
    finishtime =time()
    print finishtime-begintime
