from utl.lay import title, line
from utl.lay import colour as cl
from utl.arch import readfloat, readint, calgpa
from utl.obj import txt, all_data, options, data

print('{}Hello, world{}'.format('\033[36m', '\033[m'))

x = 0
while True:
    title('GPA - Calculator')
    for c in options:
        x = x + 1
        print(f'{cl["b"]}{x}{cl["limit"]} - {c}')
    ask = readint('Option: ')
    #show data base
    if ask == 1:
        for c in range(0, len(all_date)):
            print(f'{all_data[c]}')
    #add subject
    elif ask == 2:
        how_many = readint('How many subject do You want: ')
        ok = True
        while ok:
            for c in range(1, how_many + 1):
                data["Subject"] = str(input('Subject: ')).title()
                data["Point"] = readint('Point: ')
                data["Credit"] = readint('Credit: ')
            print(data)
            ask_data = str(input(f'It is ok [ {cl["b"]}Y | {cl["r"]}N{cl["limit"]} ]? ')).title()[0]

    #tutorial
    elif ask == 3:
        print(txt)
    #matadata
    elif ask == 4:
        print(my_data)
    #exit
    elif ask == 5:
        break