from utl.lay import title, colour, line, options
from utl.arch import readfloat, readint, grade, select, points, credits, all, calgpa, txt, gradeusa, allusa

answer = ''
arch = 'bigdate.txt'
print('{}Hello, world.{}'.format('\033[34m', '\033[m'))
title(f'GPA')
nm = str(input('Your name: ')).strip().title()
line()
while True:
    for k, i in enumerate(options):
        print(f'{colour["b"]}{k + 1}{colour["limit"]} - {i}')
    line(37)
    opt = readint('Option: ')
    if opt == 1:
        #Show database
        try:
            title(nm, 87)
            for i in select:
                print(f'{colour["b"]}{i:<40}{colour["limit"]}', end='')
            print('\n')
            for c in allusa:
                for i in c.values():
                    i = str(i)
                    if len(i) >= 30:
                        i = str(f'{i}...')
                    print(f'{i:<40}', end='')
                print()
            line(87)
            gp = x = y = w = 0
            omega = len(all)
            for count in range(0, omega):
                y = points[count] * credits[count]
                x += y
                w += credits[count]
            gp = (x / w)
            calgpa(gp)
            line(87)
        except:
            print('')
    elif opt == 2:
        #add subject
        a = readint('How many subject: ')
        for c in range(1, a + 1):
            line(30)
            grade["subject"] = str(input(f'  {c}˚ Subject: ')).strip().title()[:30]
            grade["points"] = readfloat('  Points: ')
            gradeusa["subject"] = grade["subject"]
            gradeusa["points"] = grade["points"]
            if grade["points"] >= 9:
                grade["points"] = 4
            elif grade["points"] >= 7:
                grade["points"] = 3
            elif grade["points"] >= 5:
                grade["points"] = 2
            elif grade["points"] >= 3:
                grade["points"] = 1
            elif grade["points"] >= 0:
                grade["points"] = 0
            grade["credits"] = readfloat('  Credits: ')
            gradeusa["credits"] = grade["credits"]
            line(30)
            all.append(grade.copy())
            allusa.append(gradeusa.copy())
            points.append(grade["points"])
            credits.append(grade["credits"])
        answer = ''
        while 'Y' in answer:
            for k, i in enumerate(all):
                print(f'{k} - {i}')
            answer = str(input('Do you want to remove any subject [Y / N]? ')).strip().title()[0]
            if answer == 'Y':
                k = readint('Type a key: ')
                del all[k]
                del points[k]
                del credits[k]
            else:
                print('...')
    elif opt == 3:
        print(txt)
        line(37)
    elif opt == 4:
        if len(all) == 0:
            print('Empty.')
            line()
        else:
            for k, i in enumerate(allusa):
                print(f'{colour["b"]}{k}{colour["limit"]} - {i["subject"]} | Points: {i["points"]}. Credits: {i["credits"]}')
            line()
            x = str(input(f'Do you want to delete any subject [{colour["b"]}Y{colour["limit"]} / {colour["r"]}N{colour["limit"]}]: ')).strip().title()[0]
            if x == 'Y':
                key = readint('Matter key: ')
                try:
                    del all[key]
                    del points[key]
                    del credits[key]
                    del allusa[key]
                except:
                    print('Invalid Command.')
            line()
    elif opt == 5:
        break
    else:
        print('Invalid command, please, try another option')
