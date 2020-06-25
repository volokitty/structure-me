# Vlad Volokitin (volokitty)

import os, sys, json, shutil

path = sys.argv[1].replace('\\', '\\\\') + '\\'

def parse(dictionary, path):    
    for key in dictionary:
        if dictionary[key] == 0: # empty folder
            print('Creating an empty folder')
            os.mkdir(path + key + r'\\')
        if dictionary[key] == 1: # file
            print('Creating a file')
            file = open(path + key, 'w')
            file.close()
        if dictionary[key] == 'jshint': # .jshintrc
            print('Creating a jshint file')
            shutil.copy2(r'..\\settings\\.jshintrc', path + r'\\.jshintrc')
        if type(dictionary[key]) == type(dictionary): # directory
            print('Creating a directory')
            os.mkdir(key)
            parse(dictionary[key], path + key + r'\\')

def main():
    f = open('test.txt', 'w')
    for i in sys.argv:
        f.write(i + '\n')
    f.close()

    f = open('path.txt', 'w')
    f.write(path)
    f.close()

    json_data = open(r'..\\settings\\settings.json', 'r')

    loaded = json.load(json_data)

    print(path)
    parse(loaded, path)

    json_data.close()

    return 0

if __name__ == "__main__":
    main()