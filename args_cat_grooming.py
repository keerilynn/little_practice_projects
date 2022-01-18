def client_list(*args):
    list = args
    counter = 1
    for a in args:
        print(f'{counter}. {a}')
        counter += 1

cat_grooming = client_list('Castor', 'Pollux', 'Trigger', 'Willow')