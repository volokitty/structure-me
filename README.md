# structure-me
A program to create a file and folder structure for your projects directly from the context menu.
All you have to do is follow the installation instructions and configure the settings.json file to fit you. 
**Let's do it together! :smile:**
![Image of structure-me](https://raw.githubusercontent.com/volokitty/structure-me/master/settings/img/structure-me.png)

# Requirements
* Python 3.4+
* winreg library

# Installation
1. Run your terminal / cmd as administrator.
2. pip install winregistry
3. Locate the repository wherever you want.
4. cd *your-directory/structure-me/scripts/*
5. python reg.py

That's all about it :smiley:! Now you can set up the *settings.json* file.

# Setting up the settings.json
A **key** is the **name** of a file or a folder.

There are four types of values
1. "emptyFile" is for creating an empty file.
```json
{
  "file-name.format": "emptyFile"
}
```

2. "emptyFolder" is for creating an empty folder.
```json
{
  "folder-name": "emptyFolder"
}
```

3. "file" is for copying **your file**. You should locate your file templates in *settings/templates*.
```json
{
  "the-same-name-as-your-template.format": "file"
}
```

4. { } is for creating folders, that should contain something.
```json
{
  "folder-name": "emptyFolder",
  "not-empty-folder": {
    "file-name.format": "emptyFile"
  }
}
```

5. Change the YOUR_PATH variable in main.py to the path where you installed the program.

# You did it!
And that's it! Good luck with all the development.

Vlad Volokitin, @volokitty. 2020
