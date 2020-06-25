# Vlad Volokitin (volokitty)

import os, sys, json, shutil

path = sys.argv[1].replace('\\', '\\\\') + '\\\\'

path_file = open('D:\\Code\\m\\path.txt', 'w')

def parse(dictionary, path='D:\\Code\\test\\'):  
    path_file.write('parse\n')
    for key in dictionary:
        if dictionary[key] == 0: # empty folder
            print('Creating an empty folder')
            path_file.write('Creating an empty folder\n')
            os.mkdir(path + key + r'\\')
        if dictionary[key] == 1: # file
            print('Creating a file')
            path_file.write('Creating a file\n')
            file = open(path + key, 'w')
            file.close()
        if dictionary[key] == 'jshint': # .jshintrc
            print('Creating a jshint file')
            path_file.write('Creating a jshint file\n')
            shutil.copy2(r'D:\\Code\\scripts\\2020\\structure-me\\settings\\.jshintrc', path + r'\\.jshintrc')
        if type(dictionary[key]) == type(dictionary): # directory
            print('Creating a directory')
            path_file.write('Creating a directory\n')
            os.mkdir(path + key + r'\\')
            parse(dictionary[key], path + key + r'\\')

def main():
    path_file.write('main\n')

    json_data = open(r'D:\\Code\\scripts\\2020\\structure-me\\settings\\settings.json', 'r')

    loaded = json.load(json_data)
    path_file.write('loaded\n')

    parse(loaded, path)

    json_data.close()

    return 0

main()
path_file.close()