import requests
from pathlib import Path
import urllib
import os
from dotenv import load_dotenv
from datetime import datetime
import common_helper_functions as chf


def fetch_nasa_earth(nasa_token, count):  # типа красивые картинки земли, вывести надо 5-10 ()
    request_url = 'https://api.nasa.gov/EPIC/api/natural/'
    params = {'api_key': nasa_token}
    try:
        response = requests.get(request_url, params=params)
        response.raise_for_status()
        urls = []
        for item in response.json():
            photo_name = item['image']
            found_date = datetime.strptime(item['date'], '%Y-%m-%d  %H:%M:%S')
            formatted_date = f'{found_date.year}/{"{:02d}".format(found_date.month)}/{"{:02d}".format(found_date.day)}'
            urls.append(f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{photo_name}.png')

        for url in urls[:count]:
            (file_name, file_extension) = chf.return_pars_name(url)
            path_to_save_files = Path(f'nasa/{file_name}{file_extension}')
            path_to_save_files.parent.mkdir(parents=True, exist_ok=True)
            photo_response = requests.get(url, params=params)
            photo_response.raise_for_status()
            with path_to_save_files.open('wb') as file:
                file.write(photo_response.content)
    except requests.exceptions.HTTPError:
        print('Вы ввели неверный токен или сформировался неверный запрос.')


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    fetch_nasa_earth(nasa_token, 2)