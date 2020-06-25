# Vlad Volokitin (volokitty)

import os, sys, json, shutil, pathlib

path = sys.argv[1]
cwd = pathlib.Path(os.getcwd())

def parse(dictionary, path):  
    for key in dictionary:
        if dictionary[key] == "emptyFolder": # empty folder
            os.mkdir(os.path.join(path, key, ''))
        if dictionary[key] == "emptyFile": # file
            file = open(os.path.join(path, key), 'w')
            file.close()
        if dictionary[key] == 'jshint': # .jshintrc
            shutil.copy2(os.path.join(cwd.parent.parent, r'settings\.jshintrc'), os.path.join(path, '.jshintrc'))
        if dictionary[key] == 'style.scss':
            shutil.copy2(os.path.join(cwd.parent.parent, r'settings\.jshintrc'), os.path.join(path, 'style.scss'))
        if type(dictionary[key]) == type(dictionary): # directory
            os.mkdir(os.path.join(path, key, ''))
            parse(dictionary[key], os.path.join(path, key, ''))

def main():
    json_data = open(r'D:\\Code\\scripts\\2020\\structure-me\\settings\\settings.json', 'r')

    loaded = json.load(json_data)

    parse(loaded, path)

    json_data.close()

    return 0

if __name__ == "__main__":
    main()