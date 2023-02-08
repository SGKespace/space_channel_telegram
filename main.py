import requests
from pathlib import Path
import urllib
import os

def fetch_spacex_last_launch():  # Весь код, относящийся к скачиванию фотографий от SpaceX
    api_url = "https://api.spacexdata.com/v5/launches/latest"
    response = requests.get(api_url)
    response.raise_for_status()
    urls = response.json()['links']['flickr']['original']
    basis_file_name = response.json()['id'] + "_"
    if not urls:
        print('Ссылки еще не выложили')
    else:
        for urls_number, url in enumerate(urls):
            path_to_save_files = Path(f'images/{basis_file_name + str(urls_number)}.jpeg')
            path_to_save_files.parent.mkdir(parents=True, exist_ok=True)
            with path_to_save_files.open('wb') as file:
                file.write(response.content)


def return_extension(url):
    spliten_url = urllib.parse.urlsplit(url)
    (file_name, file_extension) = os.path.splitext(spliten_url.path)
    return file_extension


def main():
   # fetch_spacex_last_launch()
   url = "https://example.com/txt/hello%20world.txt?v=9#python"
   file_extension = return_extension(url)


if __name__ == '__main__':
    main()