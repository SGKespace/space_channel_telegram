import requests
from pathlib import Path
import urllib
import os


def fetch_spacex_last_launch(launche_id: str = 'latest'):  # Весь код, относящийся к скачиванию фотографий от SpaceX
    api_url = f"https://api.spacexdata.com/v5/launches/{launche_id}"
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
            photo_response = requests.get(url)
            photo_response.raise_for_status()
            with path_to_save_files.open('wb') as file:
                file.write(photo_response.content)


if __name__ == '__main__':
    # launche_id = '5eb87d42ffd86e000604b384'
    fetch_spacex_last_launch()

