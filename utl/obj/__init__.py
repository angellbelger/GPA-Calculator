from utl.lay import colour as cl

options = ['View List', 'Add', 'Instructions', 'Metadata ', 'Exit']

txt = f'''
{cl["b"]}
Hi, I'm here to explain the system.
Option 1: View what has been added so far.
Option 2: Add stories in addition to those already in the system.
Option 3: These are instructions, you are in it right now.
Option 4: Metadata, information added to lists and dictionaries.
Option 5: To exit. {cl["limit"]}\n\n'''

allData = []
data = {}
dataUSA = {}