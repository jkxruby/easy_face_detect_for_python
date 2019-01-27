
#!/usr/bin/env python3
# -*- coding: utf-8 -*-




import pyperclip

text = pyperclip.paste()
# TODO: Separate lines and add stars.

lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '*' + lines[i]  # add star to each string in "lines" list

text = '\n'.join(lines)
pyperclip.copy(text)
mm = pyperclip.paste()
#mm1 = str(mm, encoding='utf-8')


print(mm)