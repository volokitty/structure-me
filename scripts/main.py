# Vlad Volokitin (volokitty)

import os, sys, json, shutil

path = sys.argv[1].replace('\\', '\\\\') + '\\\\'

def parse(dictionary, path='D:\\Code\\test\\'):  
    for key in dictionary:
        if dictionary[key] == 0: # empty folder
            os.mkdir(path + key + r'\\')
        if dictionary[key] == 1: # file
            file = open(path + key, 'w')
            file.close()
        if dictionary[key] == 'jshint': # .jshintrc
            shutil.copy2(r'D:\\Code\\scripts\\2020\\structure-me\\settings\\.jshintrc', path + r'\\.jshintrc')
        if type(dictionary[key]) == type(dictionary): # directory
            os.mkdir(path + key + r'\\')
            parse(dictionary[key], path + key + r'\\')

def main():
    json_data = open(r'D:\\Code\\scripts\\2020\\structure-me\\settings\\settings.json', 'r')

    loaded = json.load(json_data)

    parse(loaded, path)

    json_data.close()

    return 0

if __name__ == "__main__":
    main()