#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import pyperclip
text = pyperclip.paste()
# Sesparate lines and add stars.
lines = text.split('\n')

for i in range(len(lines)): # loop through all indexes for "lines" list
    if '-' in str(lines[i]):
        lines[i] = lines[i].replace('-','.') 
        print('replaced ',lines[i])
    elif len(lines[i]) == 10:
        lines[i] = f'{lines[i][0:3]}.{lines[i][3:6]}.{lines[i][6:]}'
        print(lines[i])
    # lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
# pyperclip.paste(text)
