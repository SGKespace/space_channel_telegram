import requests
from pathlib import Path
import urllib
import os
import common_helper_functions as chf


def fetch_spacex_last_launch(launche_id: str = 'latest'):  # Весь код, относящийся к скачиванию фотографий от SpaceX
    api_url = f"https://api.spacexdata.com/v5/launches/{launche_id}"
    response = requests.get(api_url)
    response.raise_for_status()
    current_response = response.json()

    urls = current_response['links']['flickr']['original']
    basis_file_name = f"{current_response['id']}_"

    if not urls:
        print('spacex: Ссылки еще не выложили')
        return

    for urls_number, url in enumerate(urls):
        path_to_save_files = Path(f'images/{basis_file_name}{str(urls_number)}.jpeg')
        path_to_save_files.parent.mkdir(parents=True, exist_ok=True)
        chf.download_file(url, path_to_save_files)
    print('spacex: файлы загружены')


if __name__ == '__main__':
    fetch_spacex_last_launch()