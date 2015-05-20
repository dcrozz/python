if __name__ == '__main__':
    from glob import glob
    file_names = glob('*.txt')
    for file_name in file_names:
        with open(file_name) as data:
            lines = data.readlines()
            sort_list = []
            for line in lines:
                cur_line = line.strip().split(',')
                sort_list.append(cur_line)
            sort_list.sort(key = lambda l : int(l[-1]))
            with open(file_name,'w') as out:
                for item in sort_list:
                    out.write(','.join(item) + '\n')
