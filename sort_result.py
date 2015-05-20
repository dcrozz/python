file_name = open('ID_days_perYear.txt')
lines = file_name.readlines()
sort_list = []
for line in lines:
    cur_line = line.strip().split(',')
    sort_list.append(cur_line)
sort_list.sort(key = lambda l : int(l[-1]))
with open('sorted_ID_days_perYear.txt','w') as out:
    for item in sort_list:
        out.write(item[0] + ',' +item[1]+ '\n')
