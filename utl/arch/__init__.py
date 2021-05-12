from utl.lay import colour

def readfloat(msg):
    while True:
        try:
            x = float(input(msg))
        except (KeyboardInterrupt):
            print(f'{colour["r"]}Keyboar Interrupt.{colour[f"limit"]}')
        except:
            print(f'{colour["r"]}Please, type a valid command.{colour["limit"]}')
            continue
        else:
            return x
        break


def readint(msg):
    while True:
        try:
            x = int(input(msg))
        except:
            print(f'{colour["r"]}Please, type a valid command.{colour["limit"]}')
            continue
        else:
            return x
        break

def calgpa(gpa=0):
    if gpa == 0:
        print(f"\nGPA: {colour['r']}{gpa:.2f}{colour['limit']} | Grade: {colour['r']}F{colour['limit']}")
    elif gpa <= 0.7:
        print(f"\nGPA: {colour['r']}{gpa:.2f}{colour['limit']} | Grade: {colour['r']}D-{colour['limit']}")
    elif gpa <= 1.0:
        print(f"\nGPA: {colour['r']}{gpa:.2f}{colour['limit']} | Grade: {colour['r']}D{colour['limit']}")
    elif gpa <= 1.3:
        print(f"\nGPA: {colour['r']}{gpa:.2f}{colour['limit']} | Grade: {colour['r']}D+{colour['limit']}")
    elif gpa <= 1.7:
        print(f"\nGPA: {colour['w']}{gpa:.2f}{colour['limit']} | Grade: {colour['w']}C-{colour['limit']}")
    elif gpa <= 2.0:
        print(f"\nGPA: {colour['w']}{gpa:.2f}{colour['limit']} | Grade: {colour['w']}C{colour['limit']}")
    elif gpa <= 2.3:
        print(f"\nGPA: {colour['w']}{gpa:.2f}{colour['limit']} | Grade: {colour['w']}C+{colour['limit']}")
    elif gpa <= 2.7:
        print(f"\nGPA: {colour['g']}{gpa:.2f}{colour['limit']} | Grade: {colour['w']}B-{colour['limit']}")
    elif gpa <= 3.0:
        print(f"\nGPA: {colour['g']}{gpa:.2f}{colour['limit']} | Grade: {colour['g']}B{colour['limit']}")
    elif gpa <= 3.3:
        print(f"\nGPA: {colour['c']}{gpa:.2f}{colour['limit']} | Grade: {colour['c']}B+{colour['limit']}")
    elif gpa <= 3.7:
        print(f"\nGPA: {colour['c']}{gpa:.2f}{colour['limit']} | Grade: {colour['c']}A-{colour['limit']}")
    elif gpa > 3.7:
        print(f"\nGPA: {colour['b']}{gpa:.2f}{colour['limit']} | Grade: {colour['b']}A{colour['limit']}")
