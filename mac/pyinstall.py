import PyInstaller.__main__
import os

# Define the paths for your data files
tasks_path = 'tasks.txt'
done_path = 'done.txt'

PyInstaller.__main__.run([
    'main.py',
    '--name=FocusPro',
    '--windowed',
    '--noconsole',
    '--icon=icon.icns',
    '--add-data', f'{tasks_path}{os.pathsep}.',
    '--add-data', f'{done_path}{os.pathsep}.',
    '--clean'  # <--- ADD THIS LINE
])
