with open('files\pi_million_digits.txt') as file_object:
    lines = file_object.readlines()
    pi_string =''
    for line in lines:
        pi_string += line.rstrip()
    birthday = input("Enter your birthday, in the form ddyyyy")
    if birthday in pi_string:
        print("Your birthday appears ")
    else:
        print("Your birthday doesnt appears ")