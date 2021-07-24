import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = 'win32GUI'

os.environ['TCL_LIBRARY'] = r'C:\Users\HOME\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6'
os.environ['TK.LIBRARY'] = r'C:\Users\HOME\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6'

executables = [cx_Freeze.Executable('Sandpad.py', base=base, icon='icon.ico.ico')]

cx_Freeze.setup(
    name = 'Sandpad Text Editor',
    options = {'build_exe':{'packages':['tkinter','os'],'include_files':['icon.ico.ico','tcl86t.dll','tk86t.dll','icons2']}},
    version = '0.01',
    description = 'Tkinter Application',
    executables = executables

)