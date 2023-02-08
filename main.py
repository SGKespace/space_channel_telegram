import requests
from pathlib import Path
import urllib
import os
from dotenv import load_dotenv


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


def return_pars_name(url):
    spliten_url = urllib.parse.urlsplit(url)
    (full_path, full_name) = os.path.split(spliten_url.path)
    return os.path.splitext(full_name)


def fetch_nasa_best_image(nasa_token, count):
    request_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': nasa_token, 'count': count}
    try:
        response = requests.get(request_url, params=params)
        response.raise_for_status()

        for urls_number, current_response in enumerate(response.json()):
            url = current_response['hdurl']
            (file_name, file_extension) = return_pars_name(url)
            path_to_save_files = Path(f'nasa/{file_name}{file_extension}')
            path_to_save_files.parent.mkdir(parents=True, exist_ok=True)
            photo_response= requests.get(url)
            photo_response.raise_for_status()
            with path_to_save_files.open('wb') as file:
                file.write(photo_response.content)

    except requests.exceptions.HTTPError:
        print('Вы ввели неверный токен или сформировался неверный запрос.')
    except requests.exceptions.ConnectionError:
        print('ConnectionError: Не могу подключиться к серверу.')
    return


def main():
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    fetch_nasa_best_image(nasa_token, 2)  # грузим 2 лучших картинки случайным образом
    fetch_spacex_last_launch()

if __name__ == '__main__':
    main()