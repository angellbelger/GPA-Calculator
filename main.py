from utl.lay import title, line
from utl.lay import colour as cl
from utl.arch import readfloat, readint, calgpa
from utl.obj import txt, allData, options, data, dataUSA

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
        if len(allData) == 0:
            print('Empty.')
        
        else:
            title('Your GPA', 57)
            print(f'{"Subject":<27} {"Point":<27} {"Credit":<27}\n')
            for c in range(0, len(allData)):
                print(f'{allData[c]["Subject"]:<27} {allData[c]["Point"]:<27} {allData[c]["Credit"]:<27}')
            line()

            sumPoints = 0
            lenData = len(allData)
            sumCredits = 0
            for c in range(0, lenData):
                sumPoints += allData[c]["Point"]
                sumCredits += allData[c]["Credit"]

            print(sumPoints)
            calgpa()

    #add subject
    elif ask == 2:
        how_many = readint('How many subject do You want: ')
        ok = True

        while ok:
            for c in range(0, how_many):
                data["Subject"] = str(input('Subject: ')).title()
                dataUSA["Subject"] = data["Subject"]
                data["Point"] = readfloat('Point: ')
                if data["Point"] >= 9:
                    dataUSA["Point"] = 4
                elif data["Point"] >= 7:
                    dataUSA["Point"] = 3
                elif data["Point"] >= 5:
                    dataUSA["Point"] = 2
                elif data["Point"] >= 3:
                    dataUSA = 1
                elif data["Point"] < 3:
                    dataUSA = 0
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
                    allData.append(data.copy())
                    data.clear()

            ok = False

    #tutorial
    elif ask == 3:
        print(txt)
        line()

    #matadata
    elif ask == 4:
        print(allData)

    #exit
    elif ask == 5:
        break