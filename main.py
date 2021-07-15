from utl.lay import title, line
from utl.lay import colour as cl
from utl.arch import readfloat, readint, calgpa
from utl.obj import txt, allData, options, data, dataUSA, allDatausa

print('{}Hello, world{}'.format('\033[36m', '\033[m'))

x = 0
while True:
    title('GPA - Calculator')
    x = 0
    for c in options:
        x = x + 1
        print(f'{cl["b"]}{x}{cl["limit"]} - {c}')
    ask = readint('\nOption: ')

    #show data base and calculate
    if ask == 1:
        if len(allData) == 0:
            print('Empty.')
        
        else:
            title('Your GPA', 62)
            print(f'{"Subject":<27} {"Point":<27} {"Credit":<27}\n')
            for c in range(0, len(allData)):
                print(f'{allData[c]["Subject"]:<27} {allData[c]["Point"]:<27} {allData[c]["Credit"]:<27}')
            line(62)

            numerator = 0
            lenData = len(allData)
            sumCredits = 0
            for c in range(0, lenData):
                numerator += allDatausa[c]["Point"] * allDatausa[c]["Credit"]
                sumCredits += allData[c]["Credit"]

            gpa = numerator / sumCredits
            calgpa(gpa)

    #add subject
    elif ask == 2:
        how_many = readint('How many subject do You want: ')
        ok = True

        while ok:
            for c in range(0, how_many):
                data["Subject"] = str(input('Subject: ')).title().strip()
                if len(data["Subject"]) >= 17:
                    data["Subject"] = str(f'{data["Subject"][0:18]}...')
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
                dataUSA["Credit"] = data["Credit"]

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
                    allDatausa.append(dataUSA.copy())
                    data.clear()
                    dataUSA.clear()

            ok = False

    #tutorial
    elif ask == 3:
        print(txt)
        line()

    #matadata Show what is going on and remove anyway if you want
    elif ask == 4:
        line()
        for index, value in enumerate(allData):
            print(f'{index} - {value["Subject"]} | {"Point"} | {"Credit"}')
        line()
        answer = str(input(print(f'Do want to delete any subject [ {cl["b"]}Y{cl["limit"]} | {cl["r"]}N{cl["limit"]}]? '))).title().strip()
        
        if answer == 'Y':
            key = readint('Type the code of the subject: ')
            del allData[key]
            del allDatausa[key]

    #exit
    elif ask == 5:
        break