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
        for place_details in response.json():
            photo_name = place_details['image']
            found_date = datetime.strptime(place_details['date'], '%Y-%m-%d  %H:%M:%S')
            formatted_date = f'{found_date.year}/{"{:02d}".format(found_date.month)}/{"{:02d}".format(found_date.day)}'
            urls.append(f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{photo_name}.png')
        if len(urls) < count:
            count = len(urls)
        for url in urls[:count]:
            (file_name, file_extension) = chf.return_pars_name(url)
            path_to_save_files = Path(f'images/{file_name}{file_extension}')
            path_to_save_files.parent.mkdir(parents=True, exist_ok=True)
            chf.download_file(url, path_to_save_files, params)
        print('NASA EPIC: Файлы загружены.')
    except requests.exceptions.HTTPError:
        print('NASA EPIC: Вы ввели неверный токен или сформировался неверный запрос.')


if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    count = 10
    fetch_nasa_earth(nasa_token, count)