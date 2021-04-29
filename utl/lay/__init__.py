colour = {'r': '\033[31m', 'g': '\033[32m', 'w': '\033[33m', 'b': '\033[34m', 'p': '\033[35m', 'c': '\033[36m', 'limit': '\033[m'}
options = ['View List', 'Add', 'Instructions', 'Metadata ', 'Exit']


def line(n=37):
    print('-' * n)


def title(txt, x=37):
    print('-' * x)
    print(f'{colour["c"]}{txt.center(x)}{colour["limit"]}')
    print('-' * x)