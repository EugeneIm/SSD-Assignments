print('THis is another test')

name = 'SSD'

def len_name():
    if len(name) == 4:
        print('four')
    else:
        print('not four')
    return len_name

print(len_name)