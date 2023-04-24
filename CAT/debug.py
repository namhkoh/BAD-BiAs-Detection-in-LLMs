input_string = '''Option 1
Option 1 
Option 1
Option 1
Option 1
Option 1
Option 3
Option 1
Option 3
Option 1
Option 1
Option 1
Option 3
Option 1
Option 1
Option 3'''

items_list = input_string.split('\n')
print(items_list)


data = ['Option 1', 'Option 1 ', 'Option 1', 'Option 1', 'Option 1', 'Option 1', 'Option 3', 'Option 1', 'Option 3', 'Option 1', 'Option 1', 'Option 1', 'Option 3', 'Option 1', 'Option 1', 'Option 3']

if items_list == data:
    print("TRUE")
else:
    print("FALSE")


