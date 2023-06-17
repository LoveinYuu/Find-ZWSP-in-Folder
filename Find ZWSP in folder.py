#!/usr/bin/env python3
import os

folder_path = input('folder path here: ')
if folder_path[-1:] != '/':
    folder_path += '/'

for file_name in os.listdir(folder_path):
    file_path = folder_path + file_name
    
    with open(file_path, 'r', encoding='utf-8') as f:
        if f.read().encode('utf-8').find(b'\xe2\x80\x8b') != -1:
            print(file_name)
