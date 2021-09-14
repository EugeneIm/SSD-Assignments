#print('THis is another test')

name = 'BCIT SSD'
sub = ':)'

def len_name():
    if len(name) == 4:
        print('four')
    else:
        print('not four')
    return len_name

len_name()

def catch_word():
    if sub in name:
        print('Inside the sentence')
    else:
        print('Not inside the sentence')
    return catch_word

catch_word()