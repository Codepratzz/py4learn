import pyperclip

text = pyperclip.paste()  # copying contents from clipboard

# seperate the text and ads the ANy sign

newText = text.split('\n')
print(newText)
print(range(len(newText)))
for lines in range(len(newText)):
    newText[lines] = '* ' + newText[lines]  # add star to each string in "lines" list
print(newText)
