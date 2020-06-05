with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('files\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('files\Golden_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

file_path = r"C:\Users\paul.bailey\Source\repos\python\LearnPython\PythonApplication1\Files\Golden_digits - Copy.txt"
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

with open('files\pi_Million_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)