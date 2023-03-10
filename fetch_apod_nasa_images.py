import requests
from pathlib import Path
import urllib
import os
from dotenv import load_dotenv
from datetime import datetime
import common_helper_functions as chf


def fetch_nasa_best_images(nasa_token, count):
    request_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': nasa_token, 'count': count}
    try:
        response = requests.get(request_url, params=params)
        response.raise_for_status()
        for place_details in response.json():
            url = place_details['hdurl']
            (file_name, file_extension) = chf.return_pars_name(url)
            path_to_save_files = Path(f'images/{file_name}{file_extension}')
            path_to_save_files.parent.mkdir(parents=True, exist_ok=True)
            chf.download_file(url, path_to_save_files)
        print('NASA APOD: Файлы загружены.')
    except requests.exceptions.HTTPError:
        print('NASA APOD: Вы ввели неверный токен или сформировался неверный запрос.')
    except requests.exceptions.ConnectionError:
        print('NASA APOD: Не могу подключиться к серверу.')
    return


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    count = 10
    fetch_nasa_best_images(nasa_token, count)

