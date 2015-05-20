def time_diff( time1, time2 ):
    """
    time2 - time1
    e.g.
    time1 : 18:12:59
    time2 : 19:53:34
    
    
    """
    h1, m1, s1 = map(int, time1.split(':'))
    h2, m2, s2 = map(int, time2.split(':'))
    
    return (h2-h1)*3600+(m2-m1)*60+(s2-s1)
    
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
        top1 = dct_sorted[-1][0]
        top2 = dct_sorted[-2][0]
        with open(file_name) as data:
            lines = data.readlines()
            #change line
            clst = []
            for line in lines:
                cur_line = line.strip().split(',')
                if (cur_line[1]==top1 and cur_line[2] ==top2) or (cur_line[1]==top2 and cur_line[2]==top1):
                    cur_line.append(str(time_diff(cur_line[-3],cur_line[-2])))
                    clst.append(cur_line)
            with open(file_name[:-4] + 'with_time_delta.txt','w') as out:
                for itm in clst:
                    out.write(','.join(itm) + '\n')
    finishtime =time()
    print finishtime-begintime
