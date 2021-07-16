from utl.lay import title, line
from utl.lay import colour as cl
from utl.arch import readfloat, readint, calgpa
from utl.obj import txt, allData, options, data, pointsUSA

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
            print(f'{cl["c"]}{"Subject":<27} {"Point":<27} {"Credit":<27}{cl["limit"]}\n')
            for c in range(0, len(allData)):
                print(f'{allData[c]["Subject"]:<27} {allData[c]["Point"]:<27} {allData[c]["Credit"]:<27}')
            line(62)

            numerator = 0
            lenData = len(allData)
            sumCredits = 0
            for c in range(0, lenData):
                numerator += pointsUSA[c] * allData[c]["Credit"]
                sumCredits += allData[c]["Credit"]

            average = numerator / sumCredits
            calgpa(average)

    #add subject
    elif ask == 2:
        how_many = readint('How many subject do You want: ')
        ok = True
        while ok:
            for c in range(0, how_many):
                data["Subject"] = str(input('Subject: ')).title().strip()
                if len(data["Subject"]) >= 17:
                    data["Subject"] = str(f'{data["Subject"][0:18]}...')
                data["Point"] = readfloat('Point: ')
                if data["Point"] >= 9:
                    pointsUSA += [4]
                elif data["Point"] >= 7:
                    pointsUSA += [3]
                elif data["Point"] >= 5:
                    pointsUSA += [2]
                elif data["Point"] >= 3:
                    pointsUSA += [1]
                elif data["Point"] < 3:
                    pointsUSA += [0]
                data["Credit"] = readint('Credit: ')
                print('\n')
                line()
                for k, v in data.items():
                    print(f'{cl["b"]}{k} - {v}{cl["limit"]}')

                line()
                print('\n')
                ask_data = str(input(f'It is ok [ {cl["b"]}Y{cl["limit"]} | {cl["r"]}N{cl["limit"]} ]? '))[0].title()

                if ask_data == 'N':
                    pointsUSA.pop()
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

    #matadata Show what is going on and remove anyway if you want
    elif ask == 4:
        line()
        for index, value in enumerate(allData):
            print(f'{cl["b"]}{index}{cl["limit"]} - {value["Subject"]} | {value["Point"]} | {value["Credit"]} | GPA: {pointsUSA[index]}')
        line()
        answer = str(input(f'Do want to delete any subject [ {cl["b"]}Y{cl["limit"]} | {cl["r"]}N{cl["limit"]}]? '))[0].title()
        
        if answer == 'Y':
            key = readint('Type the code of the subject: ')
            del allData[key]
            del pointsUSA[key]

    #exit
    elif ask == 5:
        break