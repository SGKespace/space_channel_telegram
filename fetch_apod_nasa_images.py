import requests
from pathlib import Path
import urllib
import os
from dotenv import load_dotenv
from datetime import datetime
import common_helper_functions as chf


def fetch_nasa_best_image(nasa_token, count):
    request_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': nasa_token, 'count': count}
    try:
        response = requests.get(request_url, params=params)
        response.raise_for_status()
        for urls_number, current_response in enumerate(response.json()):
            url = current_response['hdurl']
            (file_name, file_extension) = chf.return_pars_name(url)
            path_to_save_files = Path(f'nasa/{file_name}{file_extension}')
            path_to_save_files.parent.mkdir(parents=True, exist_ok=True)
            photo_response = requests.get(url)
            photo_response.raise_for_status()
            with path_to_save_files.open('wb') as file:
                file.write(photo_response.content)
    except requests.exceptions.HTTPError:
        print('Вы ввели неверный токен или сформировался неверный запрос.')
    except requests.exceptions.ConnectionError:
        print('ConnectionError: Не могу подключиться к серверу.')
    return


if __name__ == '__main__':
    print('Тут только функции')