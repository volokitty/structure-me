import os, sys, winreg

cwd = os.getcwd()
main_script = sys.executable
key_path = r'Directory\Background\shell\structureME'
key = winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, key_path)
# winreg.SetValue(key, '', winreg.REG_SZ, '')
winreg.SetValueEx(key, 'Icon', 0, winreg.REG_SZ, main_script + f' "{cwd}\\main.py"')


command_key = winreg.CreateKeyEx(key, 'command')
winreg.SetValue(command_key, '', winreg.REG_SZ, main_script + f' "{cwd}\\main.py"')
