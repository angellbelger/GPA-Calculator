from utl.lay import title, line
from utl.lay import colour as cl
from utl.arch import readfloat, readint, calgpa
from utl.obj import txt, all_data, options, data

print('{}Hello, world{}'.format('\033[36m', '\033[m'))

x = 0
while True:
    title('GPA - Calculator')
    x = 0
    for c in options:
        x = x + 1
        print(f'{cl["b"]}{x}{cl["limit"]} - {c}')
    ask = readint('\nOption: ')

    #show data base
    if ask == 1:
        if len(all_data) == 0:
            print('Empty.')
        
        else:
            title('Your GPA', 57)
            for c in range(0, len(all_data)):
                print(f'{all_data[c]["Subject"]:<27} {all_data[c]["Point"]:<27} {all_data[c]["Credit"]:<27}')
            line()

    #add subject
    elif ask == 2:
        how_many = readint('How many subject do You want: ')
        ok = True

        while ok:
            for c in range(0, how_many):
                data["Subject"] = str(input('Subject: ')).title()
                data["Point"] = readfloat('Point: ')
                data["Credit"] = readint('Credit: ')
                print('\n')
                line()
                for k, v in data.items():
                    print(f'{cl["b"]}{k} - {v}{cl["limit"]}')

                line()
                print('\n')
                ask_data = str(input(f'It is ok [ {cl["b"]}Y{cl["limit"]} | {cl["r"]}N{cl["limit"]} ]? ')).title()[0]

                if ask_data == 'N':
                    print(f'\n{cl["r"]}Data not registered.{cl["limit"]}\n')

                else:
                    print(f'\n{cl["c"]}Data registered.{cl["limit"]}\n')
                    all_data.append(data.copy())
                    data.clear()

            ok = False

    #tutorial
    elif ask == 3:
        print(txt)

    #matadata
    elif ask == 4:
        print(all_data)

    #exit
    elif ask == 5:
        break