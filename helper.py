import requests
import datetime
import time
import pytz
import os
import json

utc = pytz.UTC

USE_LOCAL_PATHS = False
if os.path.exists('local_paths.json'):
    USE_LOCAL_PATHS = True
    print("\nWARNING: USING LOCAL DEPENDENCY PATHS\n-------------------------------------------------------------------\n\n\n")
    with open('local_paths.json') as f:
        LOCAL_PATH_JSON = json.load(f)

def __parse_path__(path, dependency_directory, d_type):
    path = path.strip()

    if path.startswith('/'):
        print(f"Provided with absolute path for dependency {id}. Please verify this is correct.")
        return path
    else:
        path_folders = path.split('/')
        if d_type != 'folder':
            print('here')
            path_folders.pop()
        print(d_type, path_folders)
        temp_path = dependency_directory
        for folder in path_folders:
            temp_path = os.path.join(temp_path, folder)

            if not os.path.exists(temp_path):
                os.makedirs(temp_path)


        return os.path.join(dependency_directory, path)

def poll_dependency(id, dependency_directory, verify_path_func=lambda path: True): # timeout and poll in seconds
    if USE_LOCAL_PATHS:
        return LOCAL_PATH_JSON[id]

    try:
        r = requests.get(f'http://ckg03.isi.edu:16321/Macroscore/result/{id}').json()
    except ValueError:
        raise Exception(f"Dependency '{id}' not found")
    return __parse_path__(r['path'], dependency_directory, r['type'])

def get_output_location(id, dependency_directory):
    if USE_LOCAL_PATHS:
        return LOCAL_PATH_JSON[id]
    try:
        r = requests.get(f'http://ckg03.isi.edu:16321/Macroscore/result/{id}').json()
    except ValueError:
        raise Exception(f"Dependency '{id}' not found")
    return __parse_path__(r['path'], dependency_directory, r['type'])

def set_output_updated(id):
    if USE_LOCAL_PATHS:
        return

    r = requests.put(f'http://ckg03.isi.edu:16321/Macroscore/result/updated/{id}').json()
    if(r['message'] != 'success'):
        raise Exception(f"Could not set {id} as updated")

    return
