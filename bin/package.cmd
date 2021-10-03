@echo off
cd ..
python install pyinstaller==4.5.1
pyinstaller -F main.py
cd bin