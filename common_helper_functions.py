import urllib
import os
import requests


def return_pars_name(url):
    spliten_url = urllib.parse.urlsplit(url)
    (full_path, full_name) = os.path.split(spliten_url.path)
    return os.path.splitext(full_name)


def download_files(url, path_to_save_files, params: str = ''):
    photo_response = requests.get(url, params=params)
    photo_response.raise_for_status()
    with path_to_save_files.open('wb') as file:
        file.write(photo_response.content)