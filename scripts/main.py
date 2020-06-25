# Vlad Volokitin (volokitty)

import os, sys, json, shutil, pathlib

path = sys.argv[1]
cwd = pathlib.Path(os.getcwd())

def parse(dictionary, path):  
    for key in dictionary:
        if dictionary[key] == 'emptyFolder': # empty folder
            os.mkdir(os.path.join(path, key, ''))

        elif dictionary[key] == 'emptyFile': # file
            file = open(os.path.join(path, key), 'w')
            file.close()

        elif type(dictionary[key]) == type(dictionary): # directory
            os.mkdir(os.path.join(path, key, ''))
            parse(dictionary[key], os.path.join(path, key, ''))

        elif dictionary[key] == 'file': # File with your data
            shutil.copy2(os.path.join(cwd.parent.parent, f'settings\\{key}'), os.path.join(path, f'{key}'))

def main():
    json_data = open(os.path.join(cwd.parent.parent, r'settings\settings.json'), 'r')

    loaded = json.load(json_data)

    parse(loaded, path)

    json_data.close()

    return 0

if __name__ == "__main__":
    main()