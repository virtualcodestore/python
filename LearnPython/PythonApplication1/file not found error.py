

def count_words(file_name):
    file_name = "Files\\" + file_name
    try:
        with open(file_name,'r',encoding = 'utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + file_name + " does not exist"
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + file_name + " has about " + str(num_words) + " words")


filenames = ['Alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']

for file_name in filenames:
    count_words(file_name)